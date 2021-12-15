var character =
    document.getElementById("character");

var block =
    document.getElementById("block");

function jump() {
    // fixes animation restarting when spamming left click
    if (character.classList.contains("animate")) {
        return
    }
    // adds class animate if animate is not added yet
    if(character.classList != "animate") {
        character.classList.add("animate");
    }
    // removes class animate so it allows users to jump more than once
    setTimeout(function(){
        character.classList.remove("animate");
    }, 500);
}

var checkDead = setInterval(function(){
    var characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    var blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));
    if (blockLeft < 40 && blockLeft > 0 && characterTop >= 260) {
        block.style.animation = "none";
        block.style.display = "none";
        alert("You Lose!");
    }
}, 10);