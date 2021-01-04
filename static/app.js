
async function processForm(evt) {
    evt.preventDefault();
    let guess = $("#guess-input").val();
    const resp = await axios.post("/make-guess", {
        guess: guess,
    });
}


$("#guess-form").on("submit", processForm);