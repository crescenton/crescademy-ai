const textarea = document.querySelector("textarea");

textarea.addEventListener("input", () => {

    textarea.style.height = "auto";

    textarea.style.height =
        textarea.scrollHeight + "px";

});

const form = document.querySelector("form");

form.addEventListener("submit", () => {

    const button =
        document.querySelector("button");

    button.innerText = "Thinking...";

    button.disabled = true;

});
