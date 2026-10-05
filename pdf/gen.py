import html
P=[]
def page(cls,body,n=None):
    P.append(f'<section class="pg {cls}">{body}<div class="rod"><b>COZA</b><span>Black Friday 2026</span><i>{n or ""}</i></div></section>')
def ph(t): return f'<span class="ph">{t}</span>'

# 1 capa
P.append('''<section class="pg capa"><div class="topo">BRIEFING DE CONTEÚDO · CREATORS</div>
<div class="logo">coza</div><h1>BLACK<br>COZA<br><em>2026</em></h1>
<p class="sub">Conteúdo pensado pra vender no site<br>Linhas Modo, Brisa, Zip Vácuo e Organizadores</p>
<div class="fotos"><img src="../img/modo13.jpg"><img src="../img/brisa8.jpg"><img src="../img/zip10.jpg"></div>
<div class="pill">UGC · <b>CONVERSÃO</b></div></section>''')

page('',f'''<span class="tag">sobre a campanha</span><h2>A Coza vai<br><b>pra Black.</b></h2>
<p>A <b>Coza</b> é marca de organização e design para casa: potes herméticos, organizadores, itens de bambu e sacos a vácuo. Peças que deixam cozinha, armário e geladeira arrumados e bonitos.</p>
<p>Na Black Friday, que cai em <b>27/11/2026</b>, o foco é <b>vender no site</b> da Coza. Por isso esta campanha é diferente de uma de reconhecimento: cada vídeo precisa mostrar o problema, o produto resolvendo, a oferta e onde comprar.</p>
<div class="box"><b>Objetivo</b><br>Criativos feitos pra performance, que a Coza vai testar nos anúncios pra descobrir quais vendem mais.</div>
<div class="fotos2"><img src="../img/modo8.jpg"><img src="../img/dry6.png"></div>''',2)

page('c2',f'''<span class="tag">calendário</span><h2>4 fases até<br><b>o Natal.</b></h2>
<div class="fase a"><small>3 a 16/11</small><h3>✨ Aquecimento</h3><p>Conteúdo de desejo: o produto resolvendo a bagunça de cozinha e armário. Chamada pro Grupo VIP / CozaLovers.</p></div>
<div class="fase b"><small>17 a 24/11</small><h3>📣 Esquenta</h3><p>Anuncia a oferta e a data. O tráfego pesado começa aqui.</p></div>
<div class="fase c"><small>25 a 30/11</small><h3>🔥 Semana da BF</h3><p>Oferta escrita na tela, urgência real e CTA direto pro site. Inclui Cyber Monday.</p></div>
<div class="fase d"><small>Dezembro</small><h3>🎁 Pós</h3><p>Mesmos criativos com ângulo de presente de Natal.</p></div>''',3)

page('c3','''<span class="tag">prazos</span><h2>Entregou até<br><b>10/11.</b></h2>
<p>O anúncio precisa de alguns dias rodando antes do pico pra descobrir qual criativo performa. Então a conta é de trás pra frente:</p>
<div class="step"><b>até 20/10</b><span>Seleção das creators e kickoff</span></div>
<div class="step"><b>3 dias</b><span>Roteiro enviado para aprovação</span></div>
<div class="step"><b>5 dias</b><span>Gravação e edição</span></div>
<div class="step"><b>aprovações</b><span>Ajustes finos, se houver</span></div>
<div class="step big"><b>10/11</b><span>Criativos finais entregues</span></div>
<p class="peq">Postagem seguindo a data combinada de cada fase.</p>''',4)

prods=[('modo13','Modular Modo 13 peças','Linha Modo','var(--cristal)'),('bambu10','Potes Modo Bambu 10 peças','Linha Modo','var(--cristal)'),('crush18','Pote Modo 1,8L Laranja Crush','Modo · cor assinatura','var(--laranja)'),
('brisa8','Kit Brisa Mesa Posta 8 peças','Linha Brisa','var(--bambu)'),('zip10','Kit Zip Vácuo 10 peças + bomba','Zip Vácuo','var(--rosa)'),('dry6','Organizador de Geladeira Dry 6L','Organizador','var(--verde)')]
cards=''.join(f'<div class="card" style="background:{c}"><img src="../img/{i}.{"png" if i=="dry6" else "jpg"}"><small>{t}</small><b>{n}</b></div>' for i,n,t,c in prods)
page('',f'<span class="tag">produtos foco</span><h2>O que queremos<br><b>na sua mão.</b></h2><p>Sempre que der, mostre o <b>kit</b> e não só a peça solta. Kits sobem o valor da compra.</p><div class="grid">{cards}</div><p class="peq">Lista completa e links no site coza.com.br. Produtos com estoque garantido: {ph("XXXX confirmar com a Coza")}</p>',5)

page('c5','''<span class="tag">argumentos de venda</span><h2>Por que<br><b>a Coza vende.</b></h2>
<ul class="chk">
<li><b>Modo é modular.</b> Os potes encaixam e empilham em todos os tamanhos. Eleito Melhor Design por voto popular no BDA 2024.</li>
<li><b>Zip Vácuo reduz o volume.</b> Roupas ocupam até 3x menos espaço. Perfeito pra armário e mala.</li>
<li><b>Brisa é bambu.</b> Visual de bancada bonita, que rende close e mesa posta.</li>
<li><b>Hermético de verdade.</b> Mantimento fresco e geladeira arrumada.</li>
<li><b>Kits.</b> Cozinha inteira organizada de uma vez, com preço somado.</li>
<li><b>Fácil de comprar.</b> Site com Pix, parcelamento e frete grátis em compras acima do valor mínimo.</li>
</ul>''',6)

page('c6','''<span class="tag">estrutura do vídeo</span><h2>Todo vídeo<br><b>tem 4 partes.</b></h2>
<div class="step"><b>1 · Problema</b><span>0 a 3s. A bagunça real, sem filtro.</span></div>
<div class="step"><b>2 · Produto</b><span>3 a 15s. Resolvendo, em uso, na mão.</span></div>
<div class="step"><b>3 · Oferta</b><span>15 a 25s. Preço e prazo escritos na tela.</span></div>
<div class="step big"><b>4 · Site</b><span>25 a 30s. Fala e escreve: coza.com.br</span></div>
<p>Se faltar uma das quatro, a pessoa assiste, curte e não clica. Vertical 9:16, legenda queimada, primeiro frame forte.</p>''',7)

def fmt(n,titulo,emoji,intro,cenas,gancho,cls):
    li=''.join(f'<div class="cena"><b>Cena {i+1}</b><p>{c}</p></div>' for i,c in enumerate(cenas))
    return f'<span class="tag">formato {n:02d} · reels</span><h2>{emoji} {titulo}</h2><p>{intro}</p>{li}<div class="box"><b>Exemplo de gancho</b><br>“{gancho}”</div>'
F=[
(1,'Comprinhas da Black','🛍️','Mostre o que você comprou na Coza e por quê. Tom de indicação, de amiga pra amiga.',['Mostre a sacola ou caixa chegando.','Tire peça por peça e diga por que comprou.','Preço de cada item escrito na tela.','Feche com o total e o site: coza.com.br.'],'Gastei R$ XX na Black da Coza e não me arrependi de nada.','c7'),
(2,'Antes e depois','🧊','Armário ou geladeira com os potes Modo ou Brisa. O contraste é o que vende.',['Abra mostrando a bagunça real, sem filtro.','Corte seco: esvazie tudo.','Monte com os potes e mostre encaixando.','Resultado final, nome do kit e preço na tela.'],'Essa geladeira me dava vergonha. Olha agora.','c8'),
(3,'Zip Vácuo na prática','🧳','Demonstração com diferença de volume visível. Prova visual vende sozinha.',['Mala ou armário lotado de roupa.','Encha o saco, use a bomba e mostre o som.','Compare o volume lado a lado.','Mostre o kit, o preço e o site.'],'Cabe tudo isso na mesma mala? Cabe.','c9'),
(4,'Montei minha cozinha com R$ X','🧮','Desafio com valor definido. O kit somado na tela aumenta o ticket.',['Defina o valor no gancho (ex: R$ 300).','Vá somando os itens na tela, um por um.','Mostre a cozinha montada.','Total final, economia e site.'],'Montei minha cozinha inteira com R$ 300 na Black da Coza.','c10'),
(5,'Lista do que vale a pena','⭐','Top 3 ou Top 5 de itens que valem na promoção, em tom de indicação.',['Número no gancho: “5 itens que valem”.','Um item por cena, usando de verdade.','Motivo em uma frase.','Feche com o que você mais usa.'],'5 coisas da Coza que valem cada centavo na Black.','c11')]
IM={1:['brisa5','cafe3','pao'],2:['modo13','dry6','ret10'],3:['zip10','fit','easy4'],4:['modo8','bambu10','crush18'],5:['frios','brisa8','easy4']}
for f in F: page(f[5],fmt(*f)+'<div class="strip">'+''.join(f'<img src="../img/{i}.{"png" if i=="dry6" else "jpg"}">' for i in IM[f[0]])+'</div>',f[0]+7)

page('c12','''<span class="tag">teste a/b</span><h2>2 versões<br><b>do gancho.</b></h2>
<p>Cada creator entrega <b>2 versões do mesmo vídeo</b>, mudando só os primeiros 3 segundos. Assim a Coza descobre qual segura mais gente.</p>
<div class="ab"><div><b>A · Problema</b><p>“Essa bagunça me dava vergonha.”</p></div><div><b>B · Número</b><p>“Gastei menos de R$ 100 e mudou minha cozinha.”</p></div></div>
<div class="box"><b>Mais ganchos pra se inspirar</b><br>“Para de gastar com pote que não fecha.”<br>“Cabe tudo isso na mesma mala? Cabe.”<br>“Se você só pode comprar uma coisa na Black, compra essa.”<br>“O que eu comprei na Coza e por que valeu.”</div>
<p class="peq">Nomeie os arquivos como NOME_A e NOME_B.</p>''',13)

page('c13',f'''<span class="tag">escopo</span><h2>O que você<br><b>entrega.</b></h2>
<ul class="chk">
<li>{ph("X")} Reels com <b>2 versões de gancho</b> (A e B)</li>
<li>{ph("X")} Combo de stories com link</li>
<li>Link de compra com <b>UTM exclusivo</b> seu</li>
<li>Cupom com o seu nome: {ph("XXXX se a Coza liberar")}</li>
<li>Direito de repost nas redes da marca por {ph("XX")} dias</li>
<li>Exclusividade: {ph("sem / XXXX")}</li>
<li>Uso em mídia paga (Partnership Ads pelo seu perfil): {ph("XXXX sim ou não")}</li>
</ul>
<div class="box"><b>Oferta da Black</b><br>{ph("XXXX desconto, frete grátis, kit e por quanto tempo")}</div>''',14)

page('c14',f'''<span class="tag">publicação</span><h2>Marcações e<br><b>datas.</b></h2>
<h4>Data de publicação</h4><p>{ph("XXXX")}</p>
<h4>Marcações obrigatórias</h4><p>{ph("@XXXX da Coza")}</p>
<h4>Hashtags</h4><p>{ph("#XXXX")}</p>
<h4>Collab</h4><p>{ph("XXXX")}</p>
<h4>Tom de voz</h4><p>Natural, de indicação, com leveza. Fale com a sua linguagem, como se estivesse contando pra uma amiga. Nada de texto de comercial.</p>
<div class="box"><b>⚠ Ponto de atenção</b><br>Respeitar os DO's e DON'Ts da marca nas próximas páginas.</div>''',15)

page('c15','''<span class="tag">direcionais</span><h2 class="ok">DO's</h2><ul class="chk ok">
<li>Mostrar o produto funcionando, em uso real</li>
<li>Preço, kit somado e prazo escritos na tela</li>
<li>Falar o nome completo do produto (ex: Pote Hermético Coza Modo 1,8L)</li>
<li>Falar e escrever coza.com.br e usar seu link/cupom</li>
<li>Usar a sua linguagem e o seu tom de voz</li>
<li>Seguir a marca nas redes e marcar</li>
<li>Legendar todos os conteúdos</li>
<li>Usar só trilhas livres de direitos autorais</li>
<li>Confirmar sempre que receber um documento</li>
</ul>''',16)
page('c16','''<span class="tag">direcionais</span><h2 class="no">DON'Ts</h2><ul class="chk no">
<li>Tampar a marca ou o nome do produto</li>
<li>Postar em datas diferentes das combinadas</li>
<li>Prometer desconto, estoque ou prazo que a Coza não confirmou</li>
<li>Vídeo sem preço, sem oferta ou sem site</li>
<li>Aparecer produto de outra marca no enquadramento</li>
<li>Abrir com “oi gente, hoje vou mostrar…”</li>
<li>Conteúdo político atrelado à marca</li>
<li>Termos pejorativos ou preconceituosos</li>
<li>Usar música com direitos autorais</li>
</ul>''',17)

P.append(f'''<section class="pg fim"><div class="logo">coza</div><h1>Bora<br>vender.</h1><p>Qualquer dúvida é só chamar!<br>{ph("contato / WhatsApp XXXX")}</p><div class="fotos"><img src="../img/crush18.jpg"><img src="../img/brisa5.jpg"><img src="../img/ret10.jpg"></div></section>''')

css='''
@page{size:1080px 1920px;margin:0}
:root{--l:#FF5A1F;--creme:#F6F1E7;--preto:#141414;--cristal:#CFE6EC;--bambu:#E3C48E;--rosa:#FFD3C2;--verde:#CFE8C8}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;color:var(--preto);font-size:36px;line-height:1.35}
.pg{width:1080px;height:1920px;position:relative;overflow:hidden;padding:110px 90px 150px;background:var(--creme);page-break-after:always;break-after:page}
h1,h2,h3{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;line-height:.98;letter-spacing:-.02em}
h2{font-size:104px;margin:20px 0 28px}h2 b{color:var(--l)}
h3{font-size:44px;margin:6px 0 10px}h4{font-size:30px;letter-spacing:.1em;text-transform:uppercase;color:#D93F0B;margin:30px 0 4px}
p{margin-bottom:24px;font-size:38px}.peq{font-size:28px;opacity:.7}
.tag{display:inline-block;background:var(--preto);color:var(--creme);font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;padding:10px 20px}
.rod{position:absolute;left:90px;right:90px;bottom:60px;display:flex;justify-content:space-between;font-size:26px;border-top:4px solid var(--preto);padding-top:18px}
.rod b{font-family:'Bricolage Grotesque';font-size:34px;color:var(--l)}.rod i{font-style:normal;font-weight:700}
.ph{color:#E00000;font-weight:700}
.box{background:var(--preto);color:var(--creme);padding:34px 40px;margin:30px 0;font-size:36px;box-shadow:10px 10px 0 var(--l)}
.box b{color:var(--l);text-transform:uppercase;letter-spacing:.1em;font-size:26px}
.capa{background:var(--l);padding:90px}.capa .topo{font-weight:700;letter-spacing:.14em;font-size:28px}
.logo{font-family:'Bricolage Grotesque';font-weight:800;font-size:90px;letter-spacing:-.04em;margin:50px 0 20px}
.capa h1{font-size:300px;text-transform:uppercase;line-height:.86}.capa h1 em{font-style:normal;color:var(--creme)}
.sub{font-size:40px;font-weight:500;margin:36px 0}
.fotos{display:flex;gap:20px;position:absolute;left:90px;right:90px;bottom:200px}
.fotos img{width:300px;height:380px;object-fit:cover;border:5px solid var(--preto);background:#fff}
.pill{position:absolute;left:90px;bottom:80px;border:4px solid var(--preto);border-radius:99px;padding:16px 40px;font-size:36px;background:var(--creme)}
.fotos2{display:flex;gap:24px;margin-top:20px}.fotos2 img{width:450px;height:520px;object-fit:cover;border:5px solid var(--preto);background:#fff;box-shadow:10px 10px 0 var(--l)}
.fase{border:5px solid var(--preto);padding:28px 36px;margin-bottom:28px;box-shadow:10px 10px 0 var(--preto)}
.fase small{font-weight:700;letter-spacing:.12em;font-size:26px;text-transform:uppercase}.fase p{font-size:32px;margin:0}
.fase.a{background:var(--cristal)}.fase.b{background:var(--bambu)}.fase.c{background:var(--l)}.fase.d{background:var(--verde)}
.step{background:#fff;border:5px solid var(--preto);padding:26px 36px;margin-bottom:24px;display:flex;flex-direction:column;box-shadow:10px 10px 0 var(--preto)}
.step b{font-family:'Bricolage Grotesque';font-size:56px;color:var(--l);line-height:1}.step span{font-size:34px}
.step.big{background:var(--preto);color:var(--creme)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:10px}
.card{border:5px solid var(--preto);padding:0 0 18px;box-shadow:8px 8px 0 var(--preto)}
.card img{width:100%;height:170px;object-fit:cover;background:#fff;border-bottom:5px solid var(--preto)}
.card small{display:block;font-size:22px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:14px 20px 0}.card b{display:block;font-size:30px;line-height:1.1;padding:4px 20px 0}
.chk{list-style:none}.chk li{font-size:36px;padding:20px 0 20px 70px;position:relative;border-bottom:3px solid rgba(0,0,0,.15)}
.chk li::before{content:"✦";position:absolute;left:0;color:var(--l);font-size:42px}
.chk.ok li::before{content:"✅"}.chk.no li::before{content:"🚫"}
h2.ok{color:#0B7A3B}h2.no{color:#D00000}
.c15{background:var(--verde)}.c16{background:var(--rosa)}.c2{background:#FFF8EA}
.cena{margin-bottom:18px;border-left:10px solid var(--l);padding-left:28px}.cena b{font-family:'Bricolage Grotesque';font-size:38px}.cena p{margin:0;font-size:34px}
.c7{background:var(--cristal)}.c8{background:var(--bambu)}.c9{background:var(--rosa)}.c10{background:var(--verde)}.c11{background:#FFE9A8}
.ab{display:flex;gap:24px}.ab div{flex:1;background:#fff;border:5px solid var(--preto);padding:30px;box-shadow:10px 10px 0 var(--preto)}.ab b{font-family:'Bricolage Grotesque';font-size:44px;color:var(--l)}.ab p{font-size:36px;margin:10px 0 0}
.strip{display:flex;gap:20px;position:absolute;left:90px;right:90px;bottom:170px}.strip img{flex:1;width:0;height:420px;object-fit:cover;border:5px solid var(--preto);background:#fff;box-shadow:8px 8px 0 var(--preto)}
.fim{background:var(--l)}.fim h1{font-size:230px;text-transform:uppercase;line-height:.86}.fim p{font-size:44px;margin-top:40px}
'''
doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet"><style>{css}</style></head><body>{"".join(P)}</body></html>'
open('briefing.html','w').write(doc)
