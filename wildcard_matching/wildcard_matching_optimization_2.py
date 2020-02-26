# coding=utf-8

"""
经过wildcard_matching_optimization_1.py中的优化以后，代码的执行效率提升了很多，但是要多次查询缓存字典，实际上如果要得到正确答案，我们还是要进行很多重复操作
如果可以省去这些重复操作就好了。

动态规划就是用来解决该问题，动态规划让求解过程变得有序，利用已经求出的结果推算下一个结果

动态规划最重要的就是找到问题前一个结果与后一个结果之间的关系，首先明确，这两个结果是什么？

根据之前的递归算法我们可以知道，我们都是通过首先判断模式串和输入串的前几个字符组成的子串进一步递归完整字符串的结果的。例如如下例子：

输入串：'abcbdk'

模式串：'*a*b?k'

按照递归算法，我们遇到*时，会进行3步递归，分别是判断 ：

1. abcbdk与 a*b?k
2. bcbdk与 a*b?k
3. bcbdk与*a*b?k

这三个是否匹配，实际上就是默认了未进行匹配的字符串已经符合模式串，因此我们可以通过这个思想创建矩阵，矩阵中的值就代表匹配结果，横纵索引代表模式串与输入串的索引，上述例子建立的矩阵如图：

      #     a     b     c     b     d     k
#

*

a

*

b

?

k

至于为何每个字符串前都加了一个#号，是因为对于*来说可能会匹配空串，这个#号就用于处理空串，接下来处理初始化问题，该矩阵如何初始化？既然都说了先进行子串的匹配，因此肯定就是先匹配模式串的子串或者输入串的子串，
实际上匹配输入串的子串是没有意义的，因为没有扩展价值，子串匹配失败和整个字符串的匹配结果影响不大，因此是按照模式串开始匹配：

      #     a     b     c     b     d     k
#     T     F     F     F     F     F     F

*     T

a

*

b

?

k

初始化完成后就是这个样子，毕竟#号代表的空串仅仅能和空串进行匹配。那么接下来就应该进行正则匹配了，那么匹配规则是什么呢？

对于？和a-z的字母很简单，对于字母来说：

dp[x][y] = dp[x-1][y-1] and str[y-1] == pattern[x-1]

实际上意义就是 如果[0,x-1]的模式串能与[0,y-1]的输入串匹配，那么必定[0,x-2]的模式串能与[0,y-2]的输入串匹配，并且模式串的第x-1个字符与输入串的第y-1个字符相同。更具体点就是

模式串：fadsedfg
输入串：fadsg

前四个字符匹配必须要求前三个字符都匹配并且，两个字符串的第四个字符匹配

至于带？的要求更少了，因为？代表任意字符，因此只需要：

dp[x][y] = dp[x-1][y-1]

最难为人的就是*号，*号代表任意串，因此考虑三种情况：

1. *代表空串

    在矩阵中如何表示空串呢？实际上不就是dp[x][y] = dp[x-1][y]么？

          #     a     b     c     b     d     k
    #     T     F     F     F     F     F     F

    *     T

    就是上面的模样，为什么这样表示呢？因为*不影响匹配结果不就是空串么？

2. *代表任意字符

    虽说是，代表任意字符，也就是代表一个字符，也就是？的模样，这里我们完善一下上面的矩阵


          #     a     b     c     b     d     k
    #     T     F     F     F     F     F     F

    *     T     T     T     T     T     T     T

    a     F     T     F     F     F     F     F

    *     F     T     T

    b

    ?

    k

    就是这里，可以看到 x=b，y=*处是T，这不就是问号的效果么？

3. *代表任意字符串

    最后考虑匹配任意字符串，其实意思就是，当前匹配到部分到结尾的部分都不用匹配了，全部都是符合的，因此就是如下模样

          #     a     b     c     b     d     k
    #     T     F     F     F     F     F     F

    *     T     T     T     T     T     T     T

    a     F     T     F     F     F     F     F

    *     F     T     T     T     T     T    T

    b

    ?

    k

这样就可以正确建立矩阵了。
"""

def remove_dup_stars(s):
    if s == '':
        return s
    p1 = ''
    label = 0
    for c in s:
        if label == 1 and c == '*':
            continue
        elif label == 0 and c == '*':
            p1 += c
            label = 1
        else:
            p1 += c
            label = 0
    return p1


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def init_dp(s,pattern):
            dp = []
            for i in range(0,len(processed_str)+1):
                temp = []
                for j in range(0,len(s)+1):
                    temp.append(False)
                dp.append(temp)
            dp[0][0] = True
            return dp

        if len(s) == 0 and len(p) == 0:
            return True
        processed_str = remove_dup_stars(p)
        dp = init_dp(s, processed_str)
        for i in range(0,len(processed_str)):
            p_c = processed_str[i]
            i_s = 0
            if p_c == '*':
                while not dp[i][i_s] and i_s < len(s):
                    i_s += 1
                dp[i+1][i_s] = dp[i][i_s]
                while i_s < len(s):
                    dp[i+1][i_s+1] = True
                    i_s += 1
            elif p_c == '?':
                for index in range(0,len(s)):
                    dp[i+1][index +1] = dp[i][index]
            else:
                for index in range(0,len(s)):
                    dp[i+1][index +1] = dp[i][index] and processed_str[i] == s[index]
        return dp[len(processed_str)][len(s)]

