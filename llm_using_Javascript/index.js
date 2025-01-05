import { CreateMLCEngine } from "@mlc-ai/web-llm";


async function main() {
    // Callback function to update model loading process 
    const initProgressCallback = (progress) => {
        console.log("Model loading progress: ", progress);
    }

    const selectedModel = "Llama-3.1-8B-Instruct-q4f32_1-MLC";

    const engine = await CreateMLCEngine(
        selectedModel,
        { initProgressCallback: initProgressCallback }, // engineConfig
    );

    const messages = [
        { role: "system", content: "You are a helpful AI assistant." },
        { role: "user", content: "Hello!" },
    ]

    const reply = await engine.chat.completions.create({
        messages,
    });
    console.log(reply.choices[0].message);
    console.log(reply.usage);

}

main();