from flask import Flask, request
import arxiv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")
model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum")

@app.route('/summary', methods=['POST'])
def generate_summary():
  # Get the search query and number of papers from the request
  search_query = request.form.get('search_query')
  num_papers = int(request.form.get('num_papers'))

  # Perform the search
  search = arxiv.Search(
    query = search_query,
    max_results = num_papers,
    sort_by = arxiv.SortCriterion.SubmittedDate
  )

  # Initialize an empty list to store the results
  results = []

  # Loop through the results and generate a summary for each article
  for result in search.results():
    # Preprocess the input text
    input_text = result.summary
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate the summary
    output = model.generate(input_ids)

    # Decode the output summary
    summary = tokenizer.decode(output[0], skip_special_tokens=True)

    # Add the result to the list
    results.append({
      'url': result.pdf_url,
      'title': result.title,
      'abstract': result.summary,
      'year': result.published,
      'summary': summary
    })

  # Return the list of results
  return {'results': results}

if __name__ == '__main__':
  app.run(debug=True)
