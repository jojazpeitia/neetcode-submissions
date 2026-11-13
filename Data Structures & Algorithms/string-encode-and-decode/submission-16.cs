public class Solution {

    public string Encode(IList<string> strs) {
        // ["Hello", "World"] --> "5#Hello5#World"
        String encode = "";
        
        foreach ( string s in strs ) {
            string length = s.Length.ToString();
            encode += length + "#" + s;
        }
        Console.WriteLine(encode);
        return encode;
    }

    public List<string> Decode(string s) {
        // "5#Hello#World" -> ["Hello", "World"]

        List<string> ans = new List<string>();

        int l = 0;
        int r = 0;

        while (r < s.Length) {
            while (s[r] != '#') {
                r += 1;
            }
            string sizeStr = s.Substring(l, r - l);
            int size =  int.Parse(sizeStr);

            String str = "";

            r += 1;

            for (int i = 0; i < size; i++) {
                str += s[r];
                r += 1;
            }

            Console.WriteLine(str);

            ans.Add(str);

            l = r;
        }
        return ans;
   }
}
