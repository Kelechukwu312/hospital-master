$(document).ready(function(){


   /*
    **this scripts connects the chat box with the users Id (For the patience)
   */
   $(".con").hide()
    $("#close").click(function (e){
         $(".con").hide()
    });

    $(".chat-btn").click(function (e){
       var wrapper = document.getElementById('img-s')
       //var dr_id = document.getElementById('dr-id')
       //dr_id.innerHTML = ''
       wrapper.innerHTML = ''
       var action = document.getElementById('action')
       action.innerHTML = ''

       var pk= $(this).attr("data-catid");
       //var cc = document.getElementById('con')
        //alert("hello :"+pk)
        var postData = {csrfmiddlewaretoken:'{{ csrf_token }}',pk:pk}
        $.ajax({
        type: 'POST',
        url: $('#url').attr("data-href"),
        data: postData,
        dataType: 'json',
        success: function (response) {//dr_id
        $('#dr-name').empty();

        var temp="<strong>"+response.dr+" "+response.otherN+"</strong>"
        $('#dr-name').append(temp);
          //alert("okaydddss "+response.image)
          var item =`
             <img src="${response.image}" />
             <input type="text" id="dr-ids" name="dr-ids" value="${response.dr_id}" hidden />
             `
          //var idd =`
          //   <input type="text" value="${response.dr_id}" hidden />
          //   `
            wrapper.innerHTML += item
          //  dr_id.innerHTML += idd
          if(response.dr_status == "True"){
                  var act =`
                <p style="color:#47fb47;font-size:13px;" id="action">Online</p>
               `
               action.innerHTML += act
          }
          if(response.dr_status == "False"){
                var act =`
                <p style="color:#47fb47;font-size:13px;" id="action">Offline</p>
               `
               action.innerHTML += act
             }




         $(".con").slideToggle("fast")
         //cc.style.display = "block";
        },
        error: function(e) {
            alert("error "+e.responseText);
            console.log(e.responseText)

        }

        });

        //$(".con").slideToggle("slow")
     });



     /*
      ** Handling direct message from Dr and patience or patience to dr.
      ** Below is the script that handles the main chat
     */
     $("#send-message-action").click(function (e){
        e.preventDefault();
        var message_c = $("#message-content").val();
        var pk= $("#dr-ids").val();
        var dr_id = document.getElementById('dr-id')
        dr_id.innerHTML = ''
        var form = document.getElementById('form')
        csrftoken = form.getElementsByTagName("input")[0].value
        //alert("view token :"+csrftoken)
         //alert("hello :"+message_c)
         //alert("Id of user :"+pk)
        var postData = {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),message_c:message_c,pk:pk}
        $.ajax({
        type: 'POST',
        url: $('#urls').attr("data-href"),
        data: postData,
        dataType: 'json',
        success: function (response) {
            //alert("Success :"+message_c)
          var item =`
           <textarea style="overflow: hidden; padding:0 20px; border:solid 1px #eaeaea;" cols="25" rows="2" id="message-content" placeholder="Enter Message"></textarea>
             `
             dr_id.innerHTML += item
        },
        error: function(e) {
            alert("error "+e.responseText);
            console.log()

        }

        });
     });


      /*
      ** reloading of the chat.
      ** Below is the script that handles the reload of the chat
     */
       var chats = document.getElementById('chats')
       var class_name;
       var all_chat;
        chats.innerHTML = ''
      setInterval(function(){
        var pk= $("#dr-ids").val();

        $.ajax({
        type: 'GET',
        url: '/reload-chat/'+pk+'/',
        success: function (response) {
            console.log("Sf :"+response)
             $('.chats').empty();
             for(var key in response.chat){
              //if(response.chat[key].Sender_back =="True"){
              //var chatV="<div>"+response.chat[key].message+"</div>";
              //}
              //$('.chats').append(chatV);
                if(response.chat[key].Sender_back =="True"){
                    class_name = "my-chat";
              all_chat = response.chat[key].message

                   var item =
                  `

                  <div class="${class_name}">
                  ${all_chat}
                  </div>

                  `
                 chats.innerHTML += item
                 }
               if(response.chat[key].reciever_back =="True"){
                    class_name = "client-chat";
                    all_chat = response.chat[key].message
                var item =
                  `

                  <div class="${class_name}">
                  ${all_chat}
                  </div>

                  `
                 chats.innerHTML += item
               }

              //}
               //var chatV="<div>"+response.chat[key].message+"</div>";
               //$('.chats').append(chatV);
              // $('#div'+response.post).removeClass("not_liked");
                //if(response.chat[key].Sender_back == 'True'){
                  //  alert("our id")
                }

               $('.chats').css({"background":"#eaeaea", "padding":"5px","overflow-y":"auto","height":"300px"});
                //var item =
               // `

                //  <div class="">
                 // ${response.all_chat}
                 // </div>

                // `
                 //chats.innerHTML += item
               //$('.chats div').addClass("my-chat");





        },
        error: function(e) {
            //alert("error "+e.responseText);
            //console.log()

        }

        });
      },1000);






  });