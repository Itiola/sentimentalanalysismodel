async function analyze() {
    const textInput = document.getElementById("inputText");
    const resultDiv = document.getElementById("result");
    const toast = document.getElementById("toast");
    const spinner = document.getElementById("spinner");
    const text = textInput.value.trim();

    resultDiv.className = "hidden";
    resultDiv.innerText = "";

    if (text === "") {
        showToast("⚠️ Please enter some text");
        return;
    }

    spinner.style.display = "flex"; // Show spinner

    try {
        const response = await fetch("http://localhost:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text }),
        });

        const data = await response.json();
        let emoji = "";

        if (data.label === "POSITIVE") {
            resultDiv.className = "positive";
            emoji = "😊";
        } else if (data.label === "NEGATIVE") {
            resultDiv.className = "negative";
            emoji = "🙁";
        } else {
            resultDiv.className = "neutral";
            emoji = "😐";
        }

        resultDiv.innerText = `${emoji} Sentiment: ${data.label} (Confidence: ${Math.round(data.score * 100)}%)`;
        resultDiv.classList.remove("hidden");
        showToast("✅ Sentiment analyzed successfully");
    } catch (error) {
        console.error(error);
        showToast("❌ Error analyzing sentiment");
    } finally {
        spinner.style.display = "none"; // Hide spinner
    }
}

// Toast helper
function showToast(message) {
    const toast = document.getElementById("toast");
    toast.innerText = message;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}
