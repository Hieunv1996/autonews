import numpy as np
from pyvi import ViTokenizer
from gensim.models import KeyedVectors
import regex as re
import traceback
import nltk
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

RE_HTML_TAG = re.compile(r'<[^>]+>')
RE_CLEAR = re.compile("\s+")


def preprocess(txt, tokenize=True):
    try:
        txt = re.sub(RE_HTML_TAG, ' ', txt)
        txt = re.sub('&.{3,4};', ' ', txt)
        if tokenize:
            txt = ViTokenizer.tokenize(txt)
        txt = txt.lower()
        txt = re.sub(RE_CLEAR, ' ', txt)
        return txt.strip()
    except:
        traceback.print_exc()
        return ''


class NewsSummarization:
    def __init__(self, w2v_file, n_cluster=5):
        self.w2v = KeyedVectors.load_word2vec_format(w2v_file)
        self.n_cluster = n_cluster

    def sentence2vector(self, sentences):
        vocab = self.w2v.wv.vocab
        X = []
        for sentence in sentences:
            words = sentence.split(" ")
            sentence_vec = np.zeros(100)
            for word in words:
                if word in vocab:
                    sentence_vec += self.w2v.wv[word]
            X.append(sentence_vec)
        return X

    def summarization(self, document):
        document = preprocess(document)
        sentences = nltk.sent_tokenize(document)
        if len(sentences) <= self.n_cluster:
            return ' '.join(sentences)
        X = self.sentence2vector(sentences)
        kmeans = KMeans(n_clusters=self.n_cluster)
        kmeans = kmeans.fit(X)
        avg = []
        for j in range(self.n_cluster):
            idx = np.where(kmeans.labels_ == j)[0]
            avg.append(np.mean(idx))
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
        ordering = sorted(range(self.n_cluster), key=lambda k: avg[k])
        summary = ' '.join([sentences[closest[idx]] for idx in ordering])
        return summary


if __name__ == '__main__':
    suma = NewsSummarization('w2v/vi.vec')
    print(suma.summarization("""
    <article class="content_detail fck_detail width_common block_ads_connect">
<table align="center" border="0" cellpadding="3" cellspacing="0" class="tplCaption"><tbody><tr><td>
<img alt="Nga bác cáo buộc kích động biểu tình áo vàng Pháp" data-natural-h="301" data-natural-width="500" src="https://i-vnexpress.vnecdn.net/2018/12/10/yellow-shirt-9058-1544447103.jpg"/></td>
</tr><tr><td>
<p class="Image">
Cảnh sát đụng độ người biểu tình ở Paris hôm 8/12. Ảnh: <em>AP.</em></p>
</td>
</tr></tbody></table><p>
"Mọi cáo buộc Nga liên quan tới biểu tình đều là vu khống. Chúng tôi coi đó là vấn đề nội bộ của Pháp. Nga không bao giờ can thiệp vào công việc nội bộ của nước khác, do chúng tôi coi trọng việc phát triển quan hệ song phương và hai quốc gia đều nỗ lực để đạt mục tiêu này", <em>TASS </em>dẫn lời phát ngôn viên Điện Kremlin hôm nay cho biết.</p><p>
Trang tin <em>The Times </em>của Anh trước đó đưa tin hàng trăm tài khoản mạng xã hội có liên quan tới Nga đang được dùng để "kích động, tăng quy mô" cuộc biểu tình tại Pháp. Giới chức Pháp đã mở cuộc điều tra, nhưng cho biết còn quá sớm để đưa ra kết luận về thông tin này.</p><p class="Normal">
Cuộc biểu tình lớn nhất 50 năm tại Pháp nổ ra từ ngày 17/11, khi hàng chục nghìn người mặc áo vàng xuống đường kêu gọi chính phủ cắt giảm thuế xăng dầu, điều chỉnh chính sách kinh tế và thể hiện sự phản đối Tổng thống Emmanuel Macron. Họ cho rằng ông Macron không quan tâm tới người dân bình thường mà chỉ đem lại lợi ích cho giới giàu.</p><p class="Normal">
Khoảng 10.000 người hôm 8/12 tràn xuống đường phố Paris đập phá, đốt xe cộ và cướp bóc các cửa hàng, gây nên hỗn loạn. Số người tham gia biểu tình khắp nước Pháp lên tới 125.000, trong đó hơn 1.700 người đã bị bắt.</p><p class="Normal">
Sau cuộc bạo loạn ở Paris, Thủ tướng Pháp Edouard Philippe tuyên bố hoãn kế hoạch tăng thuế xăng dầu, nhưng động thái này chưa thể ngăn người dân xuống đường biểu tình. Tổng thống Macron dự kiến có bài phát biểu trước cả nước trong hôm nay.</p> </article>
    """))
