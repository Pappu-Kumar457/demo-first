// let todo=[];
// let req=prompt("please enter your request");

// while(true){
//     if(req=='quit'){
//         console.log("quitting app");
//         break;
//     }
//     if(req=="list"){
//         console.log("-----------");
//         for(let i=0;i<todo.length;i++){
//             console.log(i,todo[i]);
//         }
//         console.log("-----------");
//     }
//     else if(req=="add"){
//        let task= prompt("please enter the task you want to add");
//        todo.push(task);
//        console.log("task added");
//     }
//     else if(req=="delete"){
//      let idx=prompt("please enter the task index");
//      todo.splice(idx,1);
//      console.log("task delete");
//     }
//     else{
//         console.log("wrong request");
//     }
//     req=prompt("please enter your request");
// }



let ul=document.querySelector("ul");
let btn=document.querySelector("button");
let inp=document.querySelector("input");

btn.addEventListener("click",function () {
    let item=document.createElement("li");
    item.innerText=inp.value;
    console.log("add");

    let delBtn=document.createElement("button");
    delBtn.innerText="delete";
    delBtn.classList.add("delete");
    

    item.appendChild(delBtn);
    ul.appendChild(item);
    inp.value=" ";
   
});

ul.addEventListener("click",function(event) {
    if(event.target.nodeName=="BUTTON"){
        let ListItem=event.target.parentElement;
        ListItem.remove();
        console.log("delete");
    }
});