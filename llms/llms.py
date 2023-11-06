
from typing import Dict
from langchain import PromptTemplate
from langchain.llms import GPT4All, Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from ctransformers import AutoConfig, AutoModelForCausalLM, Config


def get_mistral():
    """
    Returns a Mistral language model for generating text.

    The model is loaded from the "models/mistral" directory and is configured with a temperature of 0.8,
    a repetition penalty of 1.2, a maximum number of new tokens of 1024, and a context length of 2048.

    Returns:
        A Mistral language model for generating text.
    """
    conf = AutoConfig(
        Config(
            temperature=0.8,
            repetition_penalty=1.2,
            max_new_tokens=1024,
            context_length=2048
        )
    )

    llm = AutoModelForCausalLM.from_pretrained(
        "models/mistral",
        config=conf,
        model_type="mistral",
        config=conf
    )
    return llm


def get_gpt4all(
        model_pth: str, 
        backend: str = 'gptj', 
        callback: bool = False
        ) -> GPT4All: 
    """
    Returns an instance of the GPT4All class, which can be used to 
    generate text using the specified model.

    Args:
        model_pth (str): The path to the model file.
        backend (str, optional): The backend to use for generating text. Defaults to 'gptj'.
        callback (bool, optional): Whether to use a callback for streaming output. Defaults to False.

    Returns:
        GPT4All: An instance of the GPT4All class.
    """
    callbacks = None
    if callback:
        callbacks = [StreamingStdOutCallbackHandler()]

    llm = GPT4All(model=model_pth, backend=backend, callbacks=callbacks)
    return llm


def get_ollama(model_name: str = 'llama2', callback: bool = False) -> Ollama:
    callback_manager = None
    if callback:
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    return Ollama(model=model_name, callback_manager=callback_manager)


def get_prompt(template: str, context: str) -> PromptTemplate:
    """
    Returns a PromptTemplate object with the given template and input variables.

    Args:
        template (str): The template string to use for the prompt.
        context (str): The context string to use for the prompt.

    Returns:
        PromptTemplate: A PromptTemplate object with the given template and input variables.
    """
    prompt = PromptTemplate(
        template=template, 
        input_variables=['question', 'context']
    ).partial(context=context)
    return prompt


def get_answer(llm, question: str) -> Dict[str, str]:
    """
    Returns a dictionary containing the answer generated by the provided language model (llm) for the given question.

    Args:
        llm: A language model object that can generate answers to questions.
        question: A string representing the question to be answered.

    Returns:
        A dictionary containing the generated answer.
    """
    return llm({'question': question})


    
