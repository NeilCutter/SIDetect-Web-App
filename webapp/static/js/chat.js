// Collapsible
const coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        this.nextElementSibling.style.maxHeight = this.nextElementSibling.style.maxHeight ? null : this.nextElementSibling.scrollHeight + "px";
    });
}

// function getTime() {
//     let today = new Date();
//     let hours = today.getHours().toString().padStart(2, '0');
//     let minutes = today.getMinutes().toString().padStart(2, '0');
//     return `${hours}:${minutes}`;
// }

// // Gets the first message
// function firstBotMessage() {
//     let firstMessage = "How's it going?";
//     document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';
    
//     let time = getTime();
    
//     $("#chat-timestamp").append(time);
//     document.getElementById("userInput").scrollIntoView(false);
// }

// firstBotMessage();

// // Retrieves the response
// function getHardResponse(userText) {
//     let botResponse = getBotResponse(userText);
//     let botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
//     $("#chatbox").append(botHtml);

//     document.getElementById("chat-bar-bottom").scrollIntoView(true);
// }

// //Gets the text text from the input box and processes it
// function getResponse() {
//     let userText = $("#textInput").val();

//     if (userText == "") {
//         userText = "We hope that SIDetect can help!";
//     }

//     let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

//     $("#textInput").val("");
//     $("#chatbox").append(userHtml);
//     document.getElementById("chat-bar-bottom").scrollIntoView(true);

//     setTimeout(() => {
//         getHardResponse(userText);
//     }, 1000)

// }

// // Handles sending text via button clicks
// function buttonSendText(sampleText) {
//     let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

//     $("#textInput").val("");
//     $("#chatbox").append(userHtml);
//     document.getElementById("chat-bar-bottom").scrollIntoView(true);

//     //Uncomment this if you want the bot to respond to this buttonSendText event
//     // setTimeout(() => {
//     //     getHardResponse(sampleText);
//     // }, 1000)
// }

// function sendButton() {
//     getResponse();
// }

// function heartButton() {
//     buttonSendText("Thank you!")
// }

// // Press enter to send a message
// $("#textInput").keypress(function (e) {
//     if (e.which == 13) {
//         getResponse();
//     }
// });