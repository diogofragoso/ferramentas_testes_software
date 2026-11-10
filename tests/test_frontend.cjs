// Verifica os dois modos do mesmo HTML sem dependências de navegador.
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const html = fs.readFileSync(path.join(__dirname, '../exemplos/app-alvo-teste/index.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];

function page(protocol, fetch) {
  const nodes = new Map();
  const document = {
    getElementById(id) {
      if (!nodes.has(id)) {
        const classes = new Set(['hidden']);
        nodes.set(id, {value:'', textContent:'', disabled:false,
          classList:{add:c=>classes.add(c), remove:c=>classes.delete(c), contains:c=>classes.has(c)},
          getContext:()=>({clearRect(){},fillRect(){}})});
      }
      return nodes.get(id);
    }
  };
  const context = vm.createContext({document, location:{protocol}, fetch,
    setTimeout:fn=>{fn();}, URL, FormData, console});
  vm.runInContext(script, context);
  return {document, context, run:code=>vm.runInContext(code, context)};
}

test('offline: login, aprovação, reprovação, validação e limpeza', async () => {
  const p = page('file:', () => {throw new Error('Offline não pode chamar rede');});
  const el = id => p.document.getElementById(id);
  await p.run('autoLogin()');
  assert.equal(el('app-screen').classList.contains('hidden'), false);
  el('student-name').value='Ana'; el('grade-1').value='8,5'; el('grade-2').value='9.5';
  await p.run('processarAvaliacao()');
  assert.equal(el('res-average').textContent, '9.0');
  assert.equal(el('res-badge').textContent, 'APROVADO');
  el('grade-1').value='4'; el('grade-2').value='5';
  await p.run('processarAvaliacao()');
  assert.equal(el('res-badge').textContent, 'REPROVADO');
  el('grade-1').value='8texto';
  await p.run('processarAvaliacao()');
  assert.equal(el('calc-error').classList.contains('hidden'), false);
  el('grade-1').value='';
  await p.run('processarAvaliacao()');
  assert.equal(el('calc-error').classList.contains('hidden'), false);
  p.run('sairSistema()');
  assert.equal(el('app-screen').classList.contains('hidden'), true);
  assert.equal(el('student-name').value, '');
});

test('online: falha de rede no login não dá acesso; resultado vem da API', async () => {
  const calls=[];
  let failure=true;
  const p=page('http:', async (url, options)=>{
    calls.push({url,options});
    if (failure) throw new Error('Servidor indisponível');
    return {ok:true, json:async()=>url.includes('login') ? {token:'token-teste'} : {media:9,status:'APROVADO'}};
  });
  const el=id=>p.document.getElementById(id);
  await p.run('autoLogin()');
  assert.equal(el('app-screen').classList.contains('hidden'), true);
  assert.equal(el('login-error').classList.contains('hidden'), false);
  failure=false;
  await p.run('autoLogin()');
  assert.equal(el('app-screen').classList.contains('hidden'), false);
  el('student-name').value='Ana';el('grade-1').value='8.5';el('grade-2').value='9.5';
  await p.run('processarAvaliacao()');
  const request=calls.at(-1);
  assert.equal(request.url,'/api/avaliacoes?latencia_ms=1800');
  assert.equal(request.options.headers.Authorization,'Bearer token-teste');
  assert.equal(el('res-average').textContent,'9.0');
  failure=true;
  await p.run('processarAvaliacao()');
  assert.equal(el('calc-error').classList.contains('hidden'),false);
  assert.equal(el('result-panel').classList.contains('hidden'),true);
  assert.equal(el('btn-processar').disabled,false);
});

test('limpar durante requisição impede um resultado antigo de reaparecer', async () => {
  let resolve;
  const response=new Promise(r=>{resolve=r;});
  const p=page('http:',()=>response);
  const el=id=>p.document.getElementById(id);
  el('student-name').value='Ana';el('grade-1').value='8';el('grade-2').value='9';
  const pending=p.run('processarAvaliacao()');
  p.run('limparFormulario()');
  resolve({ok:true,json:async()=>({media:8.5,status:'APROVADO'})});
  await pending;
  assert.equal(el('result-panel').classList.contains('hidden'),true);
  assert.equal(el('loading-box').classList.contains('hidden'),true);
});
