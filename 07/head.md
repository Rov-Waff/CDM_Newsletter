# 编辑部专版 - 一个速度和C++不分伯仲的编程语言

我在Github找项目的时候看到这么个项目：编程语言速度测评，这个仓库测评的结果是这样的：
| Language | Time, s | Memory, MiB | Energy, J |
| :--------------------- | -----------------------: | ------------------------------------------------: | -------------------------: |
| Scala (Staged) | 0.425<sub>±0.017</sub> | 208.26<sub>±02.66</sub> + 36.81<sub>±04.81</sub> | 27.57<sub>±01.62</sub> |
| Racket (Staged) | 0.885<sub>±0.000</sub> | 105.98<sub>±00.09</sub> + 0.00<sub>±00.00</sub> | 34.27<sub>±00.03</sub> |
| Rust | 1.012<sub>±0.000</sub> | 2.00<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 42.99<sub>±00.30</sub> |
| C++/g++ | 1.095<sub>±0.002</sub> | 3.38<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 45.08<sub>±00.23</sub> |
| C/gcc | 1.111<sub>±0.001</sub> | 1.50<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 46.73<sub>±00.25</sub> |
| D/gdc | 1.118<sub>±0.002</sub> | 6.75<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 48.63<sub>±00.23</sub> |
| C/clang | 1.138<sub>±0.001</sub> | 1.38<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 48.14<sub>±00.11</sub> |
| C++/clang++ | 1.166<sub>±0.000</sub> | 2.88<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 49.24<sub>±01.17</sub> |
| D/ldc2 | 1.167<sub>±0.001</sub> | 3.12<sub>±00.06</sub> + 0.00<sub>±00.00</sub> | 49.12<sub>±00.20</sub> |
| Nim/gcc | 1.168<sub>±0.001</sub> | 1.94<sub>±00.06</sub> + 0.00<sub>±00.00</sub> | 48.20<sub>±00.22</sub> |
| Java | 1.188<sub>±0.000</sub> | 42.25<sub>±00.11</sub> + 0.81<sub>±00.06</sub> | 48.12<sub>±00.33</sub> |
| V/gcc | 1.198<sub>±0.001</sub> | 2.12<sub>±00.00</sub> + 0.00<sub>±00.00</sub> | 47.85<sub>±00.12</sub> |
| Vala/gcc | 1.210<sub>±0.001</sub> | 5.38<sub>±00.06</sub> + 0.00<sub>±00.00</sub> | 50.36<sub>±00.52</sub> |
| Kotlin/JVM | 1.227<sub>±0.002</sub> | 44.92<sub>±00.09</sub> + 0.88<sub>±00.12</sub> | 51.69<sub>±00.13</sub> |

> Brainfuck解释速度测试，Scala和Racket是只测试了部分数据

可见，Rust语言所用的时间和所用的内存略少于C++，而在其他Benchmark中，Rust的速度也都和C++不分伯仲。并且，Linux内核现在已经有了Rust写的代码，这成功勾引了我的兴趣，这个语言都有那些特色呢？

## 号称C++杀手

Rust语言由Mozzila工程师Hoare设计的编程语言，设计它的目的就是为了解决C/C++的内存安全和并发问题，在[Rust官网](https://www.rust-lang.org/zh-CN/)上，官方指出了Rust的核心特点：高性能，可靠性，生产力。

### 生产力

先从生产力说起：Rust作为一门正在迅速发展的编程语言，更新比较频繁，常用Python的同学总需要更新Python,更新的时候所有的全局安装的Package都会丢失，而Rust官方提供了`rustup`这个工具来帮助你安装Rust编译工具链、离线文档。熟悉C/C++的同学知道，C/C++的生态十分破碎，构建一个现代化的C++项目需要用到gcc工具链编译，cmake生成Makefile，vcpkg管理第三方包，这些都需要你自己安装。而Rust则用一个自带的包管理工具——Cargo搞定了项目管理的问题，不仅是编译和下载包，它还可以自动生成文档，自动发布，自动测试。你可以参考官方的[Cargo文档](https://doc.rust-lang.org/cargo/index.html)来了解更多用法。Rust还提供了官方的类似PyPI的包仓库[Crates.io](https://crates.io/)，方便我们找包。并且，所有的包的文档都被存储在了官方统一的[文档网站](https://docs.rs)上

### 可靠性

写Java的同学应该对这个东西很熟悉...

```java
public class test{
	public static void main(String args[]){
		String n=null;
		System.out.println(n.split(" "));
	}
}

```

这样的代码是可以通过编译的，但是运行的时候仍然会报错，也就是我们熟悉的NPE：

```
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "String.split(String)" because "<local1>" is null
	at test.main(test.java:4)
```

这还只是普通应用程序的空指针报错，但是，能写出这样的空指针Bug的还有C/C++这些用来写操作系统的编程语言，而没做空指针判断而捅的篓子最出名的就是Windows大蓝屏事故，这个事故的原因就是系统驱动没有做空指针错误处理，别的地方也没有catch住这个空指针错误，导致这个错误一路冲到顶层，也就是我们看到的机场、银行的Windows系统蓝屏

而Rust是没有null这个概念的，对于可能缺失的值，Rust使用`Option<T>`枚举代替null，需要使用的时候，必须处理有值和空值两种分支的情况，否则编译器会直接报错：

```rust
use rand::Rng;

fn none_or_some() -> Option<i32> {
    let a = rand::rng().random_bool(1.0 / 3.0);
    match a {
        true => Some(1),
        false => None,
    }
}

fn main() {
    loop {
        match none_or_some() {
            Some(res) => println!("{}", res),
            None => println!("空！"),
        }
    }
}

```

这样做的好处就是编译器逼你考虑要不要处理空指针，相应的，对于错误处理，Rust也用类似的`Result<T,E>`枚举来逼你考虑错误处理，这个枚举包含两个值：`Ok`和`Err`，正常运行的时候返回携带返回值的Ok，出现错误的时候返回Err：

```rust
use std::{fs::File, io::Read};

fn ok_or_err() -> Result<String, std::io::Error> {
    let mut file = File::open("test.txt")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn main() {
    match ok_or_err() {
        Ok(res) => println!("{}", res),
        Err(_) => {
            eprintln!("Err")
        }
    }
}

```

问各位，如果我们开10个线程，对着同一个变量`int a=0`,`a+=1`十次，理论上来讲，这个变量最终的值为100,但实际上结果会远小于这个数，这就是因为发生了数据竞争，这还是好的，一些情况下操作系统发现多个线程同时访问一个内存地址会强制终止进程，还会导致数据结构破坏等问题，这就需要设计Lock来防止竞争。而Rust通过所有权模型来防止数据竞争，堆内存上的一片空间只能被一个指针指向，用一个例子来演示:

```rust
fn main(){
    let str1=String::from("Rust");
    let str2=str1;
    println!("{}",str1);
}
```

这段代码看似是把str1的值赋值给str2,但实际上，String是存储在堆内存上的，str1是一个指针，`let str2=str1`实际上是把str1指向的内存空间的所有权转交给str2，str1丢失了这片内存空间的所有权，无法访问，如果尝试访问，就会被Rust编译器发现，然后报一个“美妙的”E0382错误，这样就有效保证了不发生数据竞争。而Rust又可以通过引用、可变引用的方式在不同的作用域内使用这片堆内存，在需要用多线程来操作数据的时候，就要使用Rc/Arc/Mutex等方式来从而防止竞争。

### 高性能

在多个benchmark中，Rust的速度都和C/C++媲美，并且比C/C++更加安全，Rust是没有垃圾回收机制的，它使用生命周期标注这个机制来避免手动管理堆内存的同时避免了GC停顿

### 多面手

类似PyPI,Rust有自己的官方包仓库Crates.io,在这里可以找到不少你想要的包，例如有用来写网站的Actix-Web，训练AI用的torch-rs，操作数据库用的sea-orm，做桌面应用用的gtk4-rs，以及有望以更好的性能取代Electron框架的Tauri，甚至可以编译出网页内嵌字节码来取代JavaScript

> 热知识：Python练AI用的PyTorch是用C语言写的

**Rust已经崛起，亿万程序必须用Rust重写！**

_吗_

## 亿万程序需要重写，但不是现在

尽管Rust又诸多优点，但我们也不能忽视它的缺点。

### 编译器，让我过吧😢

在之前的介绍中就出现了引用 不可变引用 所有权模型 借用 生命周期 等概念，这些概念比较难以理解，这些东西都是需要你直面的，否则Rust编译器是不会给你过的，你往往需要花费一些时间和编译器搏斗，来处理各种所有权转移 生命周期不够长等问题，这也导致Rust的初期开发效率很低

### `cargo build --release`中，少话

Rust编译器在编译时会为了避免你写出低级错误，需要对你的代码进行大量的分析，这就拉长了编译时间，同时，Rust使用LLVM作为编译后端，这个编译后端会做大量的优化，OIer可以理解为开O2优化，可以提高性能防止TLE,但是拉长了编译时间，特别是在附上了了`--release`这个编译选项，编译时间会被进一步拉长。

### 生态还在发展

尽管Crates.io有不少库，但是Rust的生态仍然在发展，Rust生态处于一种什么都能做，什么都做不到最好的地位，例如想要做Web后端可以用中间件生态成熟的Express或Django，使用Actix就要需要手写一些中间件，并且需要直面所有权模型，带来的只有你一般用不到的上万QPS，开发效率远不如JavaScript或Python

### 编程界原神

Rust固然是一门很有价值的语言，但它的缺点不能忽视，但Rust社区存在一群“邪教徒”去其他社区里贬低其他语言，鼓吹Rust，这种人很像什么？原p！因此，Rust就得了个编程界原神的称呼

### 防呆不防傻

Rust的各种安全设计如果遇上偷懒的人滥用`unwarp`Rust也会原地panic

## 做它该做的事

记住一句话：做Rust工程师不做Rust邪教徒。我们列举几点Rust适合做的事情：

- 写操作系统 所有权模型和生命周期模型让Rust能够避免低级错误导致的操作系统崩溃
- 超高并发Web应用 Actix框架QPS轻松上万
- 军事 航空 航天 金融等对安全性要求较高的领域
- 云原生 这一块有望和Go语言搏一搏
- 嵌入式 开
- OI 理论上适合，但是实际需要看CCF的脸色

当然，如果你是喜欢探求计算机极限的计算机科学爱好者，也可以考虑让Rust做一些工程领域不会让Rust做的事情，比如用Actix写博客。Rust仍然是一个小众的生态，如果你想，欢迎为Crates.io贡献一些有趣的库！

> 由于Rust的小众特性，对写Rust的刻板印象通常是用Archlinux，系统上安装着客制化终端和终端化窗口管理器的……男娘？（坏了我占两个，半个男娘）
