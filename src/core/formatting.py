
class WordFrequencyShortFormFormatter:

    def __init__(self, summary):
        self._summary = summary

    def format(self, **kwargs):
        shortform_summary = []
        for word_summary in self._summary:
            word = word_summary.get('word')
            doc_summaries = word_summary.get('documents')
            document_count = len(doc_summaries.keys())
            sentence_count = len([sentence for doc_sentences in doc_summaries.values() for sentence in doc_sentences])
            shortform_summary.append({
                'word': word,
                'documents': document_count,
                'sentences': sentence_count
            })
        return tuple(shortform_summary)
