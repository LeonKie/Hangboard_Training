from prompt_toolkit import prompt


with ProgressBar() as pb:
    for i in pb(range(100),label=label):
        global current_time
        time.sleep(1)

    