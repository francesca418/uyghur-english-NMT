import sys
from nltk.translate.bleu_score import corpus_bleu

gold_file = sys.argv[1]
pred_file = sys.argv[2]

preds = open(pred_file, "r").readlines()
golds = open(gold_file, "r").readlines()

def evaluate(preds, golds):
    hypotheses = [pred.split() for pred in preds]
    references = [[gold.split()] for gold in golds]
    score = corpus_bleu(hypotheses=hypotheses, list_of_references=references)
    return score

score = evaluate(preds, golds)
print("BLEU Score: " + str(score * 100))