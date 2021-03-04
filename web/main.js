function f() {
        var input = document.getElementById("theBox");
        input.addEventListener("keypress", function(e) {
          if (e.key === 'Enter' || e.keyCode === 13) {
                  e.preventDefault();
                    var Token = input.value;
                        eel.run_bot(Token);
          }
        });
}

function changeMessage(x) {
    var Message = document.getElementById("theMessage")
    var input = document.getElementById("theBox");
    if (x == 'error'){
        input.value = '';
        Message.style.color = 'red';
        Message.style.fontWeight = 'bold';
        Message.style.fontStyle = 'normal';
        //Message.style.marginLeft = '10px';
        Message.innerText = "Error: please try another token";
    }
    else {
        input.value = '';
        Message.style.color = 'green';
        Message.style.fontWeight = 'bold';
        Message.style.fontStyle = 'normal';
        Message.style.marginLeft = '40px';
        Message.innerText = "Bot has started running";
    }
}
eel.expose(changeMessage);




//function f() {
//        var box = document.getElementById("theBox");
//        //box.innerHTML = eel.f1();
//        eel.f1(box.innerText);
//}