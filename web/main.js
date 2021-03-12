function f() {
        var input = document.getElementById("theBox");
        var input2 = document.getElementById("theBox2");
        input.addEventListener("keypress", function(e) {
          if (e.key === 'Enter' || e.keyCode === 13) {
                  e.preventDefault();
                    var Token = input.value;
                    var ChannelID = input2.value;
                    if (Token != '' && ChannelID != ''){
                        changeMessage('starting');
                        eel.run_bot(Token,ChannelID);
                    }
                        
          }
        });

        input2.addEventListener("keypress", function(e) {
          if (e.key === 'Enter' || e.keyCode === 13) {
                  e.preventDefault();
                    var Token = input.value;
                    var ChannelID = input2.value;
                    if (Token != '' && ChannelID != ''){
                        changeMessage('starting');
                        eel.run_bot(Token,ChannelID);
                    }
                        
          }
        });
}

function changeMessage(x) {
    var Message = document.getElementById("theMessage");
    var input = document.getElementById("theBox");
    var input2 = document.getElementById("theBox2");
    //var formm = document.getElementById('theForm');
    if (x == 'error1'){
        //alert(formm);
        //input.value = '';
        var l1 = document.getElementById('label1');
        l1.remove();
        var l2 = document.getElementById('label2');
        l2.remove();
        input.remove();
        input2.remove();
        
        Message.style.color = 'red';
        Message.style.fontWeight = 'bold';
        Message.style.fontStyle = 'normal';
        Message.innerText = "Error: please try another token.";
    }
    else if (x == 'error2'){
        //alert(formm);
        //input.value = '';
        var l1 = document.getElementById('label1');
        l1.remove();
        var l2 = document.getElementById('label2');
        l2.remove();
        input.remove();
        input2.remove();
        
        Message.style.color = 'red';
        Message.style.fontWeight = 'bold';
        Message.style.fontStyle = 'normal';
        Message.innerText = "Error: please try another channel ID.";
    }
    else if (x == 'starting'){
        //input.value = '';
        Message.innerText = "starting bot...";
    }
    else {
        //input.value = '';
        input.remove();
        input2.remove();
        var l1 = document.getElementById('label1');
        l1.remove();
        var l2 = document.getElementById('label2');
        l2.remove();
        Message.style.color = 'green';
        Message.style.fontWeight = 'bold';
        Message.style.fontStyle = 'normal';
        Message.style.marginLeft = '40px';
        Message.innerText = "Bot has started running. To stop it, just close this window.";
    }
}
eel.expose(changeMessage);