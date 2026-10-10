const fs=require('fs'),vm=require('vm');
const ctx={console,Date};vm.createContext(ctx);
vm.runInContext(fs.readFileSync('content.js','utf8')+'\n;globalThis.__l=lessons;globalThis.__s=START_DATE;',ctx);
const L=ctx.__l;
const ids=Object.keys(L).map(Number).sort((a,b)=>a-b);
const out=ids.map(id=>Object.assign({id},L[id],{
  sections:(L[id].sections||[]).map(s=>{
    if(s.type==='case'){ const blk=s.cases||s.items||[]; return Object.assign({},s,{cases:blk}); }
    return s;
  })
}));
fs.writeFileSync('/tmp/lessons.json', JSON.stringify(out));
console.log('导出课程数:', out.length);
console.log('起始日:', ctx.__s.toISOString().slice(0,10));
