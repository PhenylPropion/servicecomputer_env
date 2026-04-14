class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        # 各文字列を処理して、アルファベットの出現回数をカウントする
        for prosessing_keyword in strs:
            count= [0]*26 # 26のアルファベットの数をカウントするリスト
            
            for alphabet in prosessing_keyword:
                count[ord(alphabet) - ord('a')] += 1 # alphabetの位置を計算して、その位置のカウントを増やす
                
            key = tuple(count) # リストはハッシュ化できないため、タプルに変換してキーとして使用する
            
            # キーがまだansに存在しない場合は、空のリストを作成してから、processing_keywordを追加する
            if key not in ans:
                ans[key] = []
            ans[key].append(prosessing_keyword)
            
        return list(ans.values())
