(function(){
var c=window.matchMedia("(prefers-reduced-motion: reduce)").matches,P=document.querySelector("nav");
function S(){
P.classList.toggle("scrolled",window.scrollY>40)
}
window.addEventListener("scroll",S,{
passive:!0
}
),S();
var E=document.getElementById("navBurger"),v=document.getElementById("navPanel");
if(E&&v){
let e=function(t){
E.setAttribute("aria-expanded",t?"true":"false"),t?(v.hidden=!1,v.setAttribute("data-open","1"),P.classList.add("scrolled")):(v.removeAttribute("data-open"),v.hidden=!0,S())
}
;
var be=e;
E.addEventListener("click",function(){
e(E.getAttribute("aria-expanded")!=="true")
}
),v.addEventListener("click",function(t){
t.target.closest("a")&&e(!1)
}
),document.addEventListener("keydown",function(t){
t.key==="Escape"&&e(!1)
}
),window.addEventListener("resize",function(){
window.innerWidth>920&&e(!1)
}
)
}
var R=window.matchMedia("(hover: hover) and (pointer: fine)").matches,m=document.querySelector(".hero"),Y=document.querySelector(".hero-img");
if(m&&Y){
var C=0,k=0,O=0,T=0,ue=c?.12:.3;
R&&!c&&(m.addEventListener("mousemove",function(e){
var t=m.getBoundingClientRect();
C=((e.clientX-t.left)/t.width-.5)*-20,k=((e.clientY-t.top)/t.height-.5)*-14
}
),m.addEventListener("mouseleave",function(){
C=0,k=0
}
));
var G=!0;
"IntersectionObserver"in window&&new IntersectionObserver(function(e){
G=e[0].isIntersecting
}
).observe(m),(function e(){
if(G){
O+=(C-O)*.06,T+=(k-T)*.06;
var t=Math.min(window.scrollY,m.offsetHeight)*ue;
Y.style.transform="translate3d("+O.toFixed(2)+"px,"+(t+T).toFixed(2)+"px,0) scale(1.12)"
}
requestAnimationFrame(e)
}
)()
}
var J=document.querySelectorAll(".reveal");
if("IntersectionObserver"in window&&!c){
var Q=new IntersectionObserver(function(e){
e.forEach(function(t){
t.isIntersecting&&(t.target.classList.add("in"),Q.unobserve(t.target))
}
)
}
,{
threshold:.12
}
);
J.forEach(function(e){
Q.observe(e)
}
)
}
else J.forEach(function(e){
e.classList.add("in")
}
);
function de(e){
var t=+e.getAttribute("data-count"),n=null,r=1500;
function a(o){
n||(n=o);
var i=Math.min((o-n)/r,1);
e.textContent=Math.round(t*(1-Math.pow(1-i,3))),i<1&&requestAnimationFrame(a)
}
requestAnimationFrame(a)
}
var X=document.querySelectorAll("[data-count]");
if("IntersectionObserver"in window){
var _=new IntersectionObserver(function(e){
e.forEach(function(t){
t.isIntersecting&&(de(t.target),_.unobserve(t.target))
}
)
}
,{
threshold:.35
}
);
X.forEach(function(e){
_.observe(e)
}
)
}
else X.forEach(function(e){
e.textContent=e.getAttribute("data-count")
}
);
var w=[{
q:"“The premium harness series cut our donning time noticeably, and every shipment has passed site audit first pass. That consistency is why we keep reordering.”",n:"Procurement Head",r:"Infrastructure & EPC Group",av:"/assets/avatar-2.jpg",ph:"/assets/slide-a.jpg"
}
,{
q:"“We needed a twin-leg lanyard built to our spec. SB’s design team prototyped it, tested it, and had it in production faster than anyone else we approached.”",n:"Safety Director",r:"Wind Energy Contractor",av:"/assets/avatar-4.jpg",ph:"/assets/slide-b2.jpg"
}
,{
q:"“As a US importer, documentation and lead times matter as much as the gear itself. SB delivers on all three, order after order.”",n:"Managing Director",r:"Safety Equipment Distributor, USA",av:"/assets/avatar-3.jpg",ph:"/assets/slide-c2.jpg"
}
,{
q:"“Their garments and PPE range let us consolidate three suppliers into one — and the quality has stayed consistent across every order since.”",n:"Operations Manager",r:"Industrial Safety Supplier",av:"/assets/avatar-1.jpg",ph:"/assets/slide-d2.jpg?v=2"
}
],K=document.getElementById("tQuote"),le=document.getElementById("tName"),fe=document.getElementById("tRole"),ve=document.getElementById("tPhoto"),B=document.getElementById("tAvatars"),b=document.getElementById("tCard");
if(K&&B&&b){
let e=function(){
var r=w[p];
K.textContent=r.q,le.textContent=r.n,fe.textContent=r.r,ve.src=r.ph,Array.prototype.forEach.call(B.children,function(a,o){
a.classList.remove("on"),o===p&&(a.offsetWidth,a.classList.add("on"))
}
)
}
,t=function(r){
if(p=(r+w.length)%w.length,c){
e(),n();
return
}
b.style.transition="opacity .25s ease",b.style.opacity="0",setTimeout(function(){
e(),b.style.opacity="1"
}
,250),n()
}
,n=function(){
clearInterval(Z),Z=setInterval(function(){
t(p+1)
}
,7e3)
}
;
var Le=e,Ie=t,Ae=n,p=0,Z;
w.forEach(function(r,a){
var o=document.createElement("span");
o.className="t-av"+(a===0?" on":"");
var i=document.createElement("img");
i.src=r.av,i.alt="Show testimonial "+(a+1),o.addEventListener("click",function(){
t(a)
}
),o.appendChild(i),B.appendChild(o)
}
);
var $=document.getElementById("tPrev"),V=document.getElementById("tNext");
$&&$.addEventListener("click",function(){
t(p-1)
}
),V&&V.addEventListener("click",function(){
t(p+1)
}
),e(),n()
}
var ee=document.getElementById("quoteForm");
ee&&ee.addEventListener("submit",function(e){
e.preventDefault();
var t=e.target,n=function(l){
return t.elements[l]&&t.elements[l].value?t.elements[l].value.trim():""
}
,r=n("type")||"General enquiry",a=(n("fname")+" "+n("lname")).trim(),o=["Name: "+a,"Company: "+(n("company")||"-"),"Phone: "+(n("phone")||"-"),"Email: "+n("email"),"Delivery country / port: "+(n("country")||"-"),"Product category: "+r,"","Message:",n("msg")],i=t.querySelector("button[type=submit]"),Ee=i?i.textContent:"";
i&&(i.disabled=!0,i.textContent="Sending…");
function we(){
location.href="mailto:"+(t.getAttribute("data-email")||"sales@sbfallprotection.com")+"?subject="+encodeURIComponent("Quote request — "+r)+"&body="+encodeURIComponent(o.join(`
`))
}
function q(l){
if(i&&(i.disabled=!1,i.textContent=Ee),!l)return we();
t.innerHTML='<h3>Thank you<em>.</em></h3><p class="respond">Your request has reached our sales desk. We typically respond within one business day.</p>'
}
var ce=t.getAttribute("data-sb-url"),z=t.getAttribute("data-sb-key");
if(!ce||!z)return q(!1);
var y=null;
try{
y=crypto.randomUUID()
}
catch{
y=null
}
fetch(ce+"/rest/v1/inquiries",{
method:"POST",headers:{
apikey:z,Authorization:"Bearer "+z,"Content-Type":"application/json",Prefer:"return=minimal"
}
,body:JSON.stringify({
id:y||void 0,name:a||null,company:n("company")||null,email:n("email")||null,phone:n("phone")||null,country:n("country")||null,category:r,message:n("msg")||null,source_page:location.pathname
}
)
}
).then(function(l){
if(!l.ok)return q(!1);
y&&fetch("/api/notify",{
method:"POST",headers:{
"Content-Type":"application/json"
}
,body:JSON.stringify({
id:y
}
),keepalive:!0
}
).catch(function(){

}
),q(!0)
}
).catch(function(){
q(!1)
}
)
}
);
var u=document.querySelector(".why-g");
if(u&&window.matchMedia("(max-width:620px)").matches&&!c){
let e=function(t){
x=!0,clearTimeout(te),te=setTimeout(function(){
x=!1
}
,t||2600)
}
;
var qe=e,x=!1,te=null;
["touchstart","pointerdown","wheel"].forEach(function(t){
u.addEventListener(t,function(){
e()
}
,{
passive:!0
}
)
}
),u.addEventListener("touchend",function(){
e(2600)
}
,{
passive:!0
}
);
var L=0,g=u.scrollLeft;
["touchend","pointerup"].forEach(function(t){
u.addEventListener(t,function(){
g=u.scrollLeft
}
,{
passive:!0
}
)
}
),(function t(n){
if(requestAnimationFrame(t),x||!L){
L=n;
return
}
var r=n-L;
if(L=n,!(r>120)){
var a=u.scrollWidth-u.clientWidth;
a<=0||(g+=r*.022,g>=a&&(g=0),u.scrollLeft=g)
}

}
)(0)
}
var d=document.querySelector(".video-blk video");
if(d){
let t=function(){
var n=d.play();
n&&n.catch&&n.catch(function(){

}
)
}
;
var Se=t,f=["/assets/showreel.mp4","/assets/showreel-2.mp4","/assets/showreel-3.mp4"],M=0;
d.muted=!0,d.playsInline=!0,d.removeAttribute("loop"),d.addEventListener("ended",function(){
M=(M+1)%f.length,d.src=f[M],t()
}
),"IntersectionObserver"in window?new IntersectionObserver(function(n){
n[0].isIntersecting?t():d.pause()
}
,{
threshold:.2
}
).observe(d):t(),document.addEventListener("touchstart",function n(){
t(),document.removeEventListener("touchstart",n)
}
,{
passive:!0,once:!0
}
)
}
var s=document.getElementById("facTrack");
if(s){
let e=function(){
var r=h.scrollWidth/2;
r>0&&h.style.setProperty("--fac-dur",r/pe+"s")
}
,t=function(){
s.classList.add("is-paused"),clearTimeout(D)
}
,n=function(r){
clearTimeout(D),D=setTimeout(function(){
s.classList.remove("is-paused")
}
,r)
}
;
var Ce=e,ke=t,Oe=n,me=Array.prototype.slice.call(s.children),h=document.createElement("div");
h.className="fac-strip";
for(var F=0;
F<2;
F++){
var j=document.createElement("div");
j.className="fac-set",me.forEach(function(r){
j.appendChild(F?r.cloneNode(!0):r)
}
),h.appendChild(j)
}
s.appendChild(h);
var pe=c?15:75;
e(),window.addEventListener("resize",e),window.ResizeObserver&&new ResizeObserver(e).observe(h);
var I=!1,ne=0,re=0,D;
R?(s.addEventListener("mousedown",function(r){
I=!0,ne=r.pageX,re=s.scrollLeft,s.classList.add("dragging"),t(),r.preventDefault()
}
),window.addEventListener("mousemove",function(r){
I&&(s.scrollLeft=re-(r.pageX-ne))
}
),window.addEventListener("mouseup",function(){
I&&(I=!1,s.classList.remove("dragging"),n(600))
}
)):(s.addEventListener("touchstart",t,{
passive:!0
}
),s.addEventListener("touchend",function(){
n(2e3)
}
,{
passive:!0
}
),s.addEventListener("touchcancel",function(){
n(400)
}
,{
passive:!0
}
))
}
var f=document.querySelectorAll(".reel video");
function ae(e){
if(e.readyState>=2){
var t=e.play();
t&&t.catch&&t.catch(function(){

}
);
return
}
e.dataset.waiting||(e.dataset.waiting="1",e.addEventListener("loadeddata",function n(){
if(e.removeEventListener("loadeddata",n),delete e.dataset.waiting,e.dataset.onscreen){
var r=e.play();
r&&r.catch&&r.catch(function(){

}
)
}

}
))
}
if(f.length&&document.addEventListener("touchstart",function e(){
document.removeEventListener("touchstart",e),f.forEach(function(t){
t.dataset.onscreen&&t.paused&&!c&&ae(t)
}
)
}
,{
passive:!0,once:!0
}
),f.length&&"IntersectionObserver"in window){
var he=new IntersectionObserver(function(e){
e.forEach(function(t){
var n=t.target;
t.isIntersecting?(n.dataset.onscreen="1",n.preload==="none"&&(n.preload="auto",n.load()),c||ae(n)):(delete n.dataset.onscreen,n.pause())
}
)
}
,{
threshold:.35
}
);
f.forEach(function(e){
e.muted=!0,e.playsInline=!0,he.observe(e)
}
)
}
var A=document.querySelectorAll(".reel-sound");
function ge(e){
return e.mozHasAudio!==void 0?e.mozHasAudio:e.audioTracks?e.audioTracks.length>0:e.webkitAudioDecodedByteCount!==void 0?e.webkitAudioDecodedByteCount>0:!0
}
if(A.forEach(function(e){
var t=e.closest(".reel").querySelector("video");
t&&t.addEventListener("playing",function n(){
setTimeout(function(){
ge(t)||(e.hidden=!0)
}
,400),t.removeEventListener("playing",n)
}
)
}
),A.forEach(function(e){
e.addEventListener("click",function(t){
t.preventDefault(),t.stopPropagation();
var n=e.closest(".reel").querySelector("video");
if(n){
var r=n.muted;
if(A.forEach(function(o){
if(o!==e){
var i=o.closest(".reel").querySelector("video");
i&&(i.muted=!0),o.setAttribute("aria-pressed","false"),o.setAttribute("aria-label","Unmute this clip")
}

}
),n.muted=!r,e.setAttribute("aria-pressed",r?"true":"false"),e.setAttribute("aria-label",r?"Mute this clip":"Unmute this clip"),r){
var a=n.play();
a&&a.catch&&a.catch(function(){

}
)
}

}

}
)
}
),A.length&&"IntersectionObserver"in window){
var ye=new IntersectionObserver(function(e){
e.forEach(function(t){
if(!t.isIntersecting){
var n=t.target.querySelector("video"),r=t.target.querySelector(".reel-sound");
n&&!n.muted&&(n.muted=!0,r&&(r.setAttribute("aria-pressed","false"),r.setAttribute("aria-label","Unmute this clip")))
}

}
)
}
,{
threshold:.2
}
);
document.querySelectorAll(".reel").forEach(function(e){
ye.observe(e)
}
)
}
var H=document.querySelector(".page-hero"),N=document.querySelector(".page-hero-media img"),U=document.querySelector(".page-hero-in");
if(H&&N){
var ie=!0;
"IntersectionObserver"in window&&new IntersectionObserver(function(e){
ie=e[0].isIntersecting
}
).observe(H);
var oe=-1;
(function e(){
if(ie){
var t=window.scrollY;
if(t!==oe){
oe=t;
var n=H.offsetHeight||1,r=Math.min(t/n,1);
N.style.transform="scale("+(1.1+r*.07).toFixed(4)+")",N.style.filter="brightness("+(1-r*.3).toFixed(3)+")",U&&!c&&(U.style.opacity=Math.max(0,1-r*1.25).toFixed(3),U.style.transform="translate3d(0,"+(t*.05).toFixed(2)+"px,0)")
}

}
requestAnimationFrame(e)
}
)()
}
var W=document.getElementById("fabTop");
if(W){
let e=function(){
W.classList.toggle("show",window.scrollY>se)
}
;
var Te=e,se=Math.max(400,window.innerHeight*.8);
window.addEventListener("scroll",e,{
passive:!0
}
),window.addEventListener("resize",function(){
se=Math.max(400,window.innerHeight*.8),e()
}
),W.addEventListener("click",function(){
window.scrollTo({
top:0,behavior:c?"auto":"smooth"
}
)
}
),e()
}

}
)();

