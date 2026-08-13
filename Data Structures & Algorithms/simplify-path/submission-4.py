class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        split_path = path.split("/")
        
        for s in split_path:
            if s == ".":
                continue
            elif res and s == "..":
                res.pop()
                continue
            elif len(s) > 0 and s != "..":
                res.append(s)
            
        return "/" + "/".join(res)