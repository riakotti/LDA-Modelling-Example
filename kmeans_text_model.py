# Parts of the code from https://github.com/MihailSalnikov/tf-idf_and_k-means


# TF - Term Frequency in a document
# IDF - Inverse Document Frequency (the impotance of term in a set of documents)
# TF-IDF - Term Frequency-Inverse Document Frequency
class TFIDF:
    def compute_idf(self, strings_list):
        n = len(strings_list)
        idf = dict.fromkeys(strings_list[0].keys(), 0)
        for l in strings_list:
            for word, count in l.items():
                if count > 0:
                    idf[word] += 1
        for word, v in idf.items():
            idf[word] = log(n / float(v))
        return self.idf

    def compute_tf(self, word_dict, l):
        tf = {}
        sum_nk = len(l)
        for word, count in word_dict.items():
            tf[word] = count / sum_nk
        return self.tf

    def compute_tf_idf(self, tf, idf):
        tf_idf = dict.fromkeys(tf.keys(), 0)
        for word, v in tf.items():
            tf_idf[word] = v * idf[word]
        return self.tf_idf
