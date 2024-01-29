# askai

Create a super shortcut to writing LLM generated answers straight to you local machine!

This guide supposes the reader knows only two things, which is how to use a UNIX terminal and also how to sign up and get API keys.

# set-up

> Follow these steps in order to set-up

🧰 install:
```
chmod a+x *.sh
./install.sh
```

📓 add relevant api ([openAI](https://openai.com/blog/openai-api), [Mistral](https://docs.mistral.ai/), etc...) keys to `.env`:
```
cp .example.env .env
```

🔦 open `bashrc`:
```
nano ~/.bashrc
```

⚗️ append:
```
alias askai="./askai/ask.sh"
``` 

⚙️ restart terminal

# run

🔥 in your terminal, type:
```
askai
```

> > your answers will be recorded in [outputs](./outputs/)