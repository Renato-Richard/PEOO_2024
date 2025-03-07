function createMenuTags(){
    let navTag = document.createElement("nav");
    let olTag = document.createElement("ol");
    let liTag1 = document.createElement("li");
    let liTag2 = document.createElement("li");
    let liTag3 = document.createElement("li");
    let liTag4 = document.createElement("li");
    let liTag5 = document.createElement("li");
    let liTag6 = document.createElement("li");
    let aTag1 = document.createElement("a");
    let aTag2 = document.createElement("a");
    let aTag3 = document.createElement("a");
    let aTag4 = document.createElement("a");
    let aTag5 = document.createElement("a");
    let aTag6 = document.createElement("a");
    return {navTag, olTag, liTag1, liTag2, liTag3, liTag4, liTag5, liTag6, aTag1, aTag2, aTag3, aTag4, aTag5, aTag6};
}
function structureMenuTags(menu){
    let bodyTag = document.querySelector("body");
    bodyTag.appendChild(menu.navTag);
    menu.navTag.appendChild(menu.olTag);
    menu.olTag.appendChild(menu.liTag1);
    menu.olTag.appendChild(menu.liTag2);
    menu.olTag.appendChild(menu.liTag3);
    menu.olTag.appendChild(menu.liTag4);
    menu.olTag.appendChild(menu.liTag5);
    menu.olTag.appendChild(menu.liTag6);
    menu.liTag1.appendChild(menu.aTag1);
    menu.liTag2.appendChild(menu.aTag2);
    menu.liTag3.appendChild(menu.aTag3);
    menu.liTag4.appendChild(menu.aTag4);
    menu.liTag5.appendChild(menu.aTag5);
    menu.liTag6.appendChild(menu.aTag6);
}
function linksMenu(menu){
    menu.aTag1.href = "planoseservicos.html";
    menu.aTag2.href = "pagamentoonline.html";
    menu.aTag3.href = "nossasunidades.html";
    menu.aTag4.href = "artigosfunerarios.html";
    menu.aTag5.href = "velorioonline.html";
    menu.aTag6.href = "faleconosco.html";
}
function textMenu(menu){
    menu.aTag1.textContent = "Planos e serviços";
    menu.aTag2.textContent = "Pagamento online";
    menu.aTag3.textContent = "Nossas unidades";
    menu.aTag4.textContent = "Artigos funerários";
    menu.aTag5.textContent = "Velório online";
    menu.aTag6.textContent = "Fale conosco";
};
function mainMenu(){
    let menu = createMenuTags();
    structureMenuTags(menu);
    linksMenu(menu);
    textMenu(menu);
};
function menu(){
    let button = document.querySelector("header div button");
    if (button){
        button.addEventListener("click", function(){
            let body = document.querySelector("body");
            body.insertBefore(navTag, body.firstChild);
            navTag.style.backgroundColor = "#73212F";
            navTag.style.height = "100vh";
            navTag.style.position = "fixed";
            navTag.style.top = "0";
            navTag.style.left = "0";
            navTag.style.zIndex = "1000";
            navTag.style.padding = "2em";
            
            
            
        });
    }
}
document.addEventListener("DOMContentLoaded", menu);