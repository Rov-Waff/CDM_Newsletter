# 编辑部专版 - 用小学数学知识结束这场加密战争

看到@贺鸣Herman5\_论坛号 试图自研“加密算法”，结果不出两个小时就被攻破，其加密过程也不公开，密钥也不公开，并且仍在尝试继续做这种没有意义的“加密”。本编辑决定用最简单的小学数学知识，介绍一个无法攻破的加密算法，结束这场加密战争，并且，加密过程完全公开。

## 生成密钥

使用这个加密算法必须要有一对密钥，分为公钥和私钥。公钥是公开的，而私钥是不能公开的。生成密钥的过程如下：

先来找两个质数，分别为$p$和$q$，这两个质数是不能公开的，并且通常特别大，这里我们为了方便计算，选取$p=3;q=11$。然后计算$n=pq=33$和$\phi(n)=(p-1)(q-1)=20$，然后选取一个和$\phi(n)=20$互质的数$e$，也就是和$\phi(n)$没有公因数的数字，我们在这里选取$e=3$，然后解关于未知数$d$的方程$(ed) mod \phi(n)=1$,解得$d=7$，此时数对$(n,e)$也就是$(33,3)$就是公钥，这一对数字要公开，数字$d$也就是7就是私钥。

> mod是求余数运算也叫做取模运算

## 加密

我们先把明文转换为对应的Unicode码$F$，如果“草”这个字在Unicode码表中对应的数字是15，$F=15$，根据公钥$(n=33,e=3)$计算出密文$m=F^e mod n$,这里得到密文是27

## 解密

公钥加密的内容必须要用私钥解密。已知密文$m=9$和加密它的公钥的对应的私钥$d=7$，明文$F$的计算过程为$F=m^d mod n$，则$F={9^7} mod {33}=15$

> 如果明文特别大，但是p,q,写的特别小，就会导致数据丢失，无法进行加密

## Python实现

```python
def generate_keys(p, q):
    """生成公钥和私钥"""
    n = p * q
    phi = (p - 1) * (q - 1)

    # 选择与phi互质的e
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # 计算d (e的模反元素)
    d = modinv(e, phi)

    # 公钥 (e, n), 私钥 (d, n)
    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    """加密明文"""
    e, n = public_key
    # 将字符转换为Unicode码点
    F = ord(plaintext)
    # 加密计算
    m = pow(F, e, n)
    return m

def decrypt(ciphertext, private_key):
    """解密密文"""
    d, n = private_key
    # 解密计算
    F = pow(ciphertext, d, n)
    # 将Unicode码点转换为字符
    return chr(F)

# 辅助函数
def gcd(a, b):
    """计算最大公约数"""
    while b != 0:
        a, b = b, a % b
    return a

def modinv(e, phi):
    """计算模反元素d (ed ≡ 1 mod phi)"""
    for d in range(3, phi):
        if (e * d) % phi == 1:
            return d
    raise ValueError("模反元素不存在")

# 示例使用
if __name__ == "__main__":
    # 给定p和q,越大越好
    p = 3
    q = 11

    # 生成密钥对
    public_key, private_key = generate_keys(p, q)
    print(f"公钥: (e={public_key[0]}, n={public_key[1]})")
    print(f"私钥: (d={private_key[0]}, n={private_key[1]})")

    # 加密示例
    plaintext = '草'
    ciphertext = encrypt(plaintext, public_key)
    print(f"加密 '{plaintext}' -> {ciphertext}")

    # 解密示例
    decrypted = decrypt(ciphertext, private_key)
    print(f"解密 {ciphertext} -> '{decrypted}'")
```

## 杀死比赛

加解密过程，密钥生成过程已经给你了，p,q是两个617位的超大的质数

公钥（Base64编码过的）

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAj+1rFATQFml/zSZxEegs
EzqweIgtxoQu41BamMVBgJF64zfxaxjgSPt9W3Fe736V74UenZIKNlQKSdm4tqod
8IBsbqzrKz36CpprZBRdsPY7MaykrYBaKT7eBk2w7E5fB1bOyeuMhzSbMLQSG/pg
Zf+pvjwoXGt8iuPyMN9olxchhOUOMncfwi9Mi4FekpirTATrl9hmahnHBTzSK2XU
kwS6bmn4IjySlVGXhNJJNhpCvrgC05TttZ4VsNUBTGjahpbjz+eJvKzHyTXzVa1o
9VJWGUs2T1BDDF3oZSKVECrtY593ADChk2Yzxo1mfSDJhawGvfH8JxQLG6PH/KP0
iwIDAQAB
-----END PUBLIC KEY-----
```

密文（Base64）

```
J6Z7JTu97dHjH8cMayxsktBWWsABlbuOEyUoRZWZPXr662qJjH0GDJt2j0lV6iB1dqeiTB9/ZV6COmesT5D7A67c4WJ6xEPkqhQrON+X8DCc/QH8zOlV4nwYUo+poXCKphEJ27tqiXKmpd0IAqVMwX4+xNi3FJeEfSXHsBEVxKA/pSdWbJpqDG3bH+Dsgv2oCmzoyh+dGTBvDKQ1D8gNOu9JUzlAK1GHty0AxcvKZAoi3SlNs26GwVXbK4qyjpY6lWEqXnsJXgq81aK+2CAbveuHOizMgAGZxq0FCmO8AN5Lcq9d5FT3HtxckQ0WEB1AsNjOEd4eKL22Sro6aVJqWQ==
```

没人能够解密，除非你是广东人，手搓出来了靓仔计算机

## 写在后面

这并不是我自己搞出来的加密算法，而是早在1970年三个数学家发现的一种加密算法，这种算法称为**RSA**，它常用于银行等对安全要求十分高的地方。如果你破解了RSA，那您就写好论文等着收到图灵奖吧。这篇文章并不是想要抨击谁，而是指出现代密码学的加密算法应当公开加密过程，而不是把算法藏着掖着，这样才能保证加密算法的可靠性。想要做出好的加密算法，应当提高自己的数学水平和编程技术力，而不是在社区发送一些无意义的加密帖子。
