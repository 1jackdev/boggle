class BoggleGame {
    constructor(boardId, secs = 60) {
        this.secs = secs;
        // this.showTimer();
        this.score = 0;
        this.words = new Set();
        this.board = "#" + boardId;

        $(".guess-form", this.board).on("submit", this.processForm.bind(this));
    }

    showWord(word) {
        $(".words", this.board).append($("<li>", { text: word }));
    }

    showMessage(msg, cls) {
        $(".msg", this.board).text(msg).removeClass().addClass(`msg ${cls}`);
    }

    async processForm(evt) {
        evt.preventDefault();
        const $guess = $(".guess", this.board);
        let guess = $guess.val();
        if (!guess) return;

        if (this.words.has(guess)) {
            this.showMessage(`Already found ${guess}`, "err");
            return;
        }

        const resp = await axios.get("/make-guess", {
            params: {
                guess: guess,
            },
        });

        if (resp.data.result === "not-word") {
            this.showMessage(`${guess} is not a valid English word`, "err");
          } else if (resp.data.result === "not-on-board") {
            this.showMessage(`${guess} is not a valid word on this board`, "err");
          } else {
            this.showWord(guess);
            this.score += guess.length;
            this.showScore();
            this.words.add(guess);
            this.showMessage(`Added: ${guess}`, "ok");
          }
        $("#guess-input").val("").focus();
    }
}
