+++
title = "Simplified Chinese reader locale"
section = "locales"
order = 16
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**简体中文** — the `zh-Hans` reader pack. Script: Han (Simplified); direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `zh-Hans` |
| **Native name** | 简体中文 |
| **Script** | Han (Simplified) |
| **Direction** | left-to-right |

Paired keywords (如果 / 否则) are single tokens needing pack keyword groups, and full/half-width punctuation collapses under NFKC normalization.

## English ↔ Simplified Chinese {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          简体中文
| ---------------  -----------
| all              全部
| and              且
| any              任一
| argmax           最大值索引
| argmin           最小值索引
| args             参数
| as               作为
| assert           断言
| async            异步
| async_generator  异流
| async_main       异步入口
| async_setup      异步备置
| async_teardown   异步收尾
| at               在
| await            等弃
| await_const      等定
| await_var        等变
| before           迄
| bench            计量
| between          间
| break            中断
| call             调用
| case             情况
| catch            捕获
| class            类
| cli              命令行
| coalesce         兜底
| column           列
| command          命令
| comptime         前缀
| const            常量
| continue         继续
| conversion       转换
| —                变换
| copy             拷贝
| count            计数
| cursor           迭代器
| debug            查看
| default          默认
| describe         验题
| description      描述
| do               执行
| elif             否则如果
| else             否则
| embed            嵌入
| empty            空集
| enum             枚举
| errors           勘误
| exit             退出
| expect_failure   预期失败
| false            假
| flaky            易碎
| fn               函数
| for              遍历
| format           格式化
| fragment         片段
| free             自由
| from             取自
| future           未来
| generator        流
| global           全局
| guard            守护
| if               如果
| implements       实现
| import           导入
| interface        契约
| internal         内部
| is               是
| kernel           内核
| lambda           闭包
| lane             车道
| let              设
| line             行
| long             详
| main             入口
| match            匹配
| max              最大
| min              最小
| module           模块
| mut              传入
| name             名称
| nan              nan
| nihil            空
| not              非
| null             皆无
| only             仅
| only_in          仅于
| operand          操作数
| option           选项
| optional         可选
| options          可选项
| or               或
| own              拥有
| panic            崩溃
| pass             静默
| per              按
| primus_quem      primus_quem
| print            显示
| private          私有
| product          求积
| protected        保护
| public           公开
| radix            radix
| range            范围
| read             读取
| readonly         不变
| reduce           归约
| ref              借自
| reject           拒绝
| rename           改名
| repeat           重复
| require          需求
| rest             其余
| return           返回
| return_await     等返
| schema           架构
| self             自身
| setup            备置
| shared           commune
| short            简
| size             维度
| skip             跳过
| spread           展开
| static           静态
| step             步
| sum              求和
| switch           选择
| tag              标签
| teardown         收尾
| test             测试
| then             则
| thread           线程
| throw            抛错
| throws           可抛
| timeout          时限
| todo             预期
| trap             陷阱
| true             真
| tuple            元组
| type             类型
| ubi              ubi
| union            判别
| unstable         不稳定
| until            到
| var              变量
| variant          构造
| vertex           顶点
| via              经由
| warn             警告
| while            当
| within           内
| wrapping         模数
| write            写入
| yield            让出
```

### Types {#types}

```text locale=la
| English      简体中文
| -----------  --------
| any          任意
| ascii        窄字串
| atomic       原子
| bool         布尔
| byte         单字节
| bytes        字节
| census       普查
| channel      通道
| char         字符
| filter       过滤器
| float        小数
| frame        帧
| instant      时刻
| int          整数
| intervallum  区间
| iterator     游标
| json         json
| list         列表
| map          映射
| matrix       矩阵
| never        永不
| none         空类型
| object       对象
| promise      期约
| queue        队列
| record       ratio
| recv         接收
| regex        regex
| saturating   饱和
| send         发送
| series       序列
| set          集合
| sparsa       稀疏
| stack        栈
| string       文本
| tensor       张量
| trapping     精确
| unknown      未知
| value        动态值
| vector       向量
| void         无值
| wrapping_ty  模数类型
```

### Intrinsics {#intrinsics}

```text locale=la
| English               简体中文
| --------------------  ----------
| abs                   绝对值
| add                   添加
| added                 已添加
| added_bias            加偏置
| all                   全部
| any                   任一
| append                追加
| apply                 应用
| approx                近似
| argmax                最大值索引
| argmin                最小值索引
| at_least              至少
| at_most               至多
| bit_and               按位与
| bit_and_assign        按位与赋值
| bit_or                按位或
| bit_or_assign         按位或赋值
| ceiling               向上取整
| clamp                 限幅
| compare_exchange      比较并交换
| complement            取补
| complemented          已取补
| contains              包含
| cos                   余弦
| create                创建
| cross                 叉积
| cross_entropy         交叉熵
| cumulate              累积
| cursor                游标
| delete                删除
| densify               稠密化
| difference            差集
| divide                除以
| divide                除法
| divided               已除以
| dot                   点积
| drop                  丢弃
| end                   结束
| ends_with             结尾是
| escape                转义
| exchange              交换
| exp                   指数
| fill                  填充
| filter                过滤
| find                  查找
| find_all              查找全部
| first                 第一个
| flatten               展平
| flip                  翻转
| flipped               已翻转
| floor                 向下取整
| formata               formata
| from_flat             由扁平构造
| gather                收集
| gelu                  gelu
| get                   获取
| greater               大于
| group                 分组
| has                   含有
| intersect             相交
| intersection          交集
| invert                求逆
| is_empty              为空
| is_subset             是子集
| is_superset           是超集
| keys                  键列表
| last                  最后一个
| layer_norm            层归一化
| length                长度
| less                  小于
| ln                    自然对数
| load                  加载
| log10                 常用对数
| lowercase             小写
| map                   变换
| matches               匹配
| materialize           物化
| matmul                矩阵乘法
| maximum               最大值
| mean                  均值
| minimum               最小值
| modulo                取模
| modulo_assign         取模赋值
| multiplied            已乘以
| multiply              乘以
| named                 命名分组
| negate                取负
| negated               已取负
| nonzero_count         非零个数
| normalize             归一化
| power                 乘方
| put                   放入
| reduce                归约
| relu                  ReLU
| remove_first          移除首项
| remove_last           移除末项
| replace               替换
| reshape               重塑
| reverse               反转
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 四舍五入
| set                   设置
| shape                 形状
| shift_left            左移
| shift_right           右移
| shifted_left          已左移
| shifted_right         已右移
| sign                  符号
| silu                  silu
| sin                   正弦
| slice                 切片
| softmax               Softmax
| sort                  排序
| sorted                已排序
| split                 分割
| sqrt                  平方根
| start                 起始
| starts_with           开头是
| store                 存储
| subtract              减去
| subtracted            已减去
| sum                   求和
| swizzle               swizzle
| symmetric_difference  对称差集
| take                  取前
| take_last             取后
| tan                   正切
| text                  文本
| transpose             转置
| trim                  修剪空白
| truncate              截断
| union                 并集
| union                 并集
| uppercase             大写
| values                值列表
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
