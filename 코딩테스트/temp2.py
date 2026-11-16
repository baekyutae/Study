# 같은 count의 key를 담을 버킷
class Bucket:
    def __init__(self, count):
        self.count = count 
        self.keys = set()
        self.prev = None
        self.next = None

class Allone:
    def __init__(self):
        self.head = Bucket(0)
        self.tail =  Bucket(0)
        self.head.next = self.tail
        self.tail.next = self.ehad
        self.bucket_of_key = {}

    def _insert_after(self, node, count):
        # 목적: 필요한 count의 버킷이 없을시 추가 
        버킷생성
        원래 버킷 옆에 추가
        return 버킷


    def _detach(self,bucket):
        # 목적: key가 더이상 없을떄 버킷 제거
        제거 대상 버킷의 next와 prev를 연결해 떼어냄


    def inc(self, key):
        if key가 버킷안에 이미 있다면:
            current = 현재 key가 들은 버킷
            target = count를 +1 하므로 옆으로 옮겨갈 버킷

            if target 버킷이 현재 없거나 current.next가 tail이라면:
                    _insert_after 로 추가

            else: # 없는 키라면
                currnet = None
                target = head.next에 위치 # 첫 key이면 count가 무조건 1이니깐 첫 버킷
                if count가 1인 버킷이 없다면:
                    _insert_after 로 추가

            target 버킷에 key값 add
            bucket_of_key[ 딕셔너리에 key:target 추가 

            if current가 None이 아니라면:
                current 버킷에서 key 제거 # count += 1 했으니
                if current 버킷이 완전 key값이 비었다면:
                    _detach(current) # 버킷 제거

    def dec(self,key):
        current = 현재 버킷

        if 현재 버킷이 count 1이라면:
            del self.bucket_of_key[key] #해시맵에서 key값 제거만

        else:
            target = current의 바로 앞 버킷
            if target이 head거나 count가 -1 작은 버킷이 아니라면:
                _insert_after로 추가

        target에 key 추가
        bucket_of_key 해시맵에 key:bucket 추가

        current 버킷에서 key 제거 
        if 버킷에 남은 key가 없으면:
            _detach(current)# 버킷도 제거



        
    