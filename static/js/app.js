async function predictText() {

    const prompt = document.getElementById("prompt").value.trim();

    const numWords = Number(
        document.getElementById("numWords").value
    );

    const predictBtn = document.getElementById("predictBtn");
    const loading = document.getElementById("loading");
    const error = document.getElementById("error");
    const resultSection = document.getElementById("resultSection");

    if (!prompt) {
        showError("Please enter a starting sentence.");
        return;
    }

    predictBtn.disabled = true;
    loading.classList.remove("hidden");
    error.classList.add("hidden");
    resultSection.classList.add("hidden");

    try {

        const response = await fetch("/api/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                prompt: prompt,
                num_words: numWords
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Prediction failed.");
        }

        document.getElementById("generatedText").textContent =
            data.generated_text;

        resultSection.classList.remove("hidden");

    }

    catch (err) {

        showError(err.message);

    }

    finally {

        loading.classList.add("hidden");
        predictBtn.disabled = false;

    }

}


function showError(message) {

    const error = document.getElementById("error");

    error.textContent = message;
    error.classList.remove("hidden");

}


function copyResult() {

    const text = document.getElementById("generatedText").textContent;

    navigator.clipboard.writeText(text);

    document.getElementById("copyBtn").textContent = "Copied!";

}