import arxiv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Get the search query and number of papers from the user
search_query = input("Enter your search query: ")
num_papers = int(input("Enter the number of papers: "))

# Perform the search
search = arxiv.Search(
  query = search_query,
  max_results = num_papers,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")
model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum")

# Loop through the results and generate a summary for each article
for i, result in enumerate(search.results(), start=1):
  print(f"\n\033[1mPaper {i}: \033[0m")
  print(f"\033[1mURL:\033[0m {result.pdf_url}")
  print(f"\033[1mTitle:\033[0m {result.title}")
  print(f"\033[1mAbstract:\033[0m {result.summary}")
  print(f"\033[1mYear:\033[0m {result.published}")
  
  # Preprocess the input text
  input_text = result.summary
  input_ids = tokenizer.encode(input_text, return_tensors='pt')

  # Generate the summary
  output = model.generate(input_ids)

  # Decode the output summary
  summary = tokenizer.decode(output[0], skip_special_tokens=True)

  # Print or save the summary as desired
  print(f"\033[1mSummary:\033[0m {summary}")
  print("\033[1m---------------------------------------------------------------------\033[0m")
