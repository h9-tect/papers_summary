# papers_summary
# ArXiv Summary

This is a Python script that searches the [ArXiv](https://arxiv.org/) repository for papers matching a specific query and generates a summary for each paper using the [BART](https://huggingface.co/transformers/model_doc/bart.html) transformer.

## Requirements

- Python 3.6 or higher
- arxiv (0.5.2)
- transformers (4.0.1)

## Usage

1. Install the required packages using `pip install -r requirements.txt`.
2. Run the script using `python arxiv_summary.py`.
3. Enter your search query and the number of papers you want to retrieve.
4. The script will output the PDF URL, title, abstract, year, and summary for each paper.

## Scheduling

To schedule the script to run at a specific time every day, you can use a tool like `cron` on a Unix-based system or `Task Scheduler` on a Windows system.

Here's an example of how you can use `cron` to schedule the script to run at 8:00 AM every day:

1. Open a terminal and type `crontab -e` to open the crontab file in your default text editor.
2. Add the following line at the end of the file: `0 8 * * * /path/to/python /path/to/arxiv_summary.py`
3. Save the file and exit.

This will run the script at 8:00 AM every day.

On a Windows system, you can use the `Task Scheduler` to schedule the script to run at a specific time. Here's an example of how you can do this:

1. Open the `Task Scheduler` and click on the `Create Basic Task` option.
2. Follow the prompts to create a new task and specify the trigger (e.g. daily at 8:00 AM) and the action (e.g. run the `arxiv_summary.py` script).
3. Save the task and make sure it is enabled.

This will run the script at the specified time every day.

## Credits

- [ArXiv](https://arxiv.org/) for the paper repository
- [Hugging Face's transformers library](https://huggingface.co/transformers/) for the BART transformer

## License

This project is licensed under the [MIT License](LICENSE).
