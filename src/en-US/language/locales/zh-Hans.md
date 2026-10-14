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

Generated from the packs; read a row across to translate one term. The Latin column is the pack key, which keys the [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latin        简体中文
| ---------------  -----------  -----------
| all              omnia        全部
| and              et           且
| any              quilibet     任一
| argmax           argmaxima    最大值索引
| argmin           argminima    最小值索引
| args             argumenta    参数
| as               ut           作为
| asc              ascendens    升序
| assert           adfirma      断言
| async            fiet         异步
| async_generator  fient        异流
| async_main       incipiet     异步入口
| async_setup      praeparabit  异步备置
| async_teardown   postparabit  异步收尾
| at               apud         在
| await            tacebit      等弃
| await_const      figendum     等定
| await_var        variandum    等变
| axis             axis         轴
| before           ante         迄
| bench            metior       计量
| between          inter        间
| break            rumpe        中断
| call             ad           调用
| case             casu         情况
| catch            cape         捕获
| class            genus        类
| cli              cli          命令行
| coalesce         vel          兜底
| column           columna      列
| command          imperium     命令
| comptime         praefixum    前缀
| const            fixum        常量
| continue         perge        继续
| conversion       conversio    转换
| —                conversion   变换
| copy             exemplum     拷贝
| count            numeratio    计数
| cursor           cursor       迭代器
| debug            vide         查看
| default          ceterum      默认
| desc             descendens   降序
| describe         probandum    验题
| description      descriptio   描述
| do               fac          执行
| elif             sin          否则如果
| else             secus        否则
| embed            insere       嵌入
| empty            vacua        空集
| enum             ordo         枚举
| errors           errata       勘误
| exit             exitus       退出
| expect_failure   erratur      预期失败
| false            falsum       假
| flaky            fragilis     易碎
| fn               functio      函数
| for              itera        遍历
| format           scriptum     格式化
| fragment         fragment     片段
| from             ex           取自
| future           futura       未来
| generator        fiunt        流
| global           ubique       全局
| guard            custodi      守护
| if               si           如果
| implements       implet       实现
| import           importa      导入
| interface        implendum    契约
| internal         interna      内部
| is               est          是
| kernel           nucleum      内核
| lambda           clausura     闭包
| lane             lane         车道
| let              sit          设
| line             lineam       行
| long             longum       详
| main             incipit      入口
| match            discerne     匹配
| max              maxima       最大
| min              minima       最小
| module           regio        模块
| mut              in           传入
| name             nomen        名称
| nan              nonnumerus   nan
| not              non          非
| null             nulla        皆无
| only             solum        仅
| only_in          solum_in     仅于
| operand          operandus    操作数
| option           optio        选项
| optional         sponte       可选
| options          optiones     可选项
| or               aut          或
| own              penes        拥有
| panic            mori         崩溃
| pass             tacet        静默
| per              pro          按
| primus_quem      primus_quem  primus_quem
| print            nota         显示
| private          privata      私有
| product          factum       求积
| protected        protecta     保护
| public           publica      公开
| radix            radix        radix
| range            ab           范围
| read             lege         读取
| readonly         immutata     不变
| reduce           reducta      归约
| ref              de           借自
| reject           reice        拒绝
| rename           verte        改名
| repeat           repete       重复
| require          requirit     需求
| rest             ceteri       其余
| return           redde        返回
| return_await     reddet       等返
| schema           schema       架构
| self             ego          自身
| setup            praepara     备置
| shared           commune      共享
| short            brevis       简
| size             magnitudo    维度
| skip             omitte       跳过
| sort             ordinata     排序
| spread           sparge       展开
| static           generis      静态
| step             per          步
| sum              summa        求和
| switch           elige        选择
| tag              tag          标签
| teardown         postpara     收尾
| test             proba        测试
| then             ergo         则
| thread           filum        线程
| throw            iace         抛错
| throws           iacit        可抛
| timeout          temporis     时限
| todo             futurum      预期
| trap             capta        陷阱
| true             verum        真
| tuple            iuncta       元组
| type             typus        类型
| ubi              ubi          ubi
| union            discretio    判别
| unstable         nondum       不稳定
| until            usque        到
| var              varia        变量
| variant          finge        构造
| vertex           vertex       顶点
| via              via          经由
| warn             mone         警告
| while            dum          当
| within           intra        内
| wrapping         modulus      模数
| write            scribe       写入
| yield            cede         让出
```

### Types {#types}

```text locale=la
| English      Latin        简体中文
| -----------  -----------  --------
| any          quidlibet    任意
| ascii        ascii        窄字串
| atomic       atomic       原子
| bool         bivalens     布尔
| byte         octetus      单字节
| bytes        octeti       字节
| census       census       普查
| channel      sermo        通道
| char         littera      字符
| clamp        clampa       钳制
| filter       filtrum      过滤器
| float        fractus      小数
| frame        scrinium     帧
| instant      instans      时刻
| int          numerus      整数
| intervallum  intervallum  区间
| iterator     cursor_t     游标
| json         json         json
| ledger       tabulae      账本
| list         lista        列表
| map          tabula       映射
| matrix       matrix       矩阵
| never        numquam      永不
| none         nihil        空类型
| object       objectum     对象
| promise      promissum    期约
| queue        queue        队列
| record       ratio        ratio
| recv         tuus         接收
| reflect      reflexa      反射
| regex        regex        regex
| saturating   saturatus    饱和
| send         meus         发送
| series       series       序列
| set          copia        集合
| sparsa       sparsa       稀疏
| stack        stack        栈
| string       textus       文本
| tensor       tensor       张量
| trapping     exactus      精确
| unknown      ignotum      未知
| value        valor        动态值
| vector       vector       向量
| void         vacuum       无值
| wrap         involuta     环绕
| wrapping_ty  modulus_t    模数类型
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latin                  简体中文
| --------------------  ---------------------  ------------
| abs                   absolutum              绝对值
| add                   adde                   添加
| added                 addita                 已添加
| added_bias            addita_bias            加偏置
| all                   omnia                  全部
| any                   quilibet               任一
| append                appende                追加
| apply                 applica                应用
| approx                approximata            近似
| argmax                argmaxima              最大值索引
| argmin                argminima              最小值索引
| at                    apud                   在
| at_least              maxime                 至少
| at_most               minime                 至多
| bit_and               coniuncta              按位与
| bit_and_assign        coniunge               按位与赋值
| bit_or                disiuncta              按位或
| bit_or_assign         disiunge               按位或赋值
| ceiling               tectum                 向上取整
| clamp                 coercere               限幅
| compare_exchange      compare_exchange       比较并交换
| complement            complementa            取补
| complemented          complementata          已取补
| contains              continet               包含
| cos                   cosinus                余弦
| count_nonzero         nonnihil               非零个数
| create                crea                   创建
| cross                 transversum            叉积
| cross_entropy         crux_entropia          交叉熵
| cumulate              cumulata               累积
| cursor                cursor                 游标
| delete                dele                   删除
| densify               densata                稠密化
| difference            differentia            差集
| difference_symmetric  symmetrica             对称差集
| divide                divida                 除以
| divide                divisio                除法
| divided               divisa                 已除以
| dot                   productum              点积
| drop                  omissa                 丢弃
| end                   terminus               结束
| ends_with             finis                  结尾是
| escape                munita                 转义
| exchange              exchange               交换
| exp                   exponentia             指数
| expanded              expande                扩展
| fill                  reple                  填充
| filter                filtrata               过滤
| find                  inventa                查找
| find_all              collecta               查找全部
| first                 primus                 第一个
| flatten               planata                展平
| flip                  alterna                翻转
| flipped               alternata              已翻转
| floor                 pavimentum             向下取整
| formata               formata                formata
| gather                gather                 收集
| gelu                  gelu                   gelu
| get                   accipe                 获取
| greater               maior                  大于
| group                 coetus                 分组
| has                   habet                  含有
| intersect             inter                  相交
| intersection          intersectio            交集
| invert                inversa                求逆
| is_empty              vacua                  为空
| is_subset             subcopia               是子集
| is_superset           supercopia             是超集
| keys                  claves                 键列表
| last                  ultimus                最后一个
| length                longitudo              长度
| less                  minor                  小于
| limes                 limes                  边界
| ln                    logarithmus            自然对数
| load                  load                   加载
| log10                 logarithmus_decimalis  常用对数
| lowercase             minuscula              小写
| map                   mappata                变换
| matches               consentit              匹配
| materialize           materialize            物化
| matmul                matmul                 矩阵乘法
| maximum               maximus                最大值
| mean                  media                  均值
| minimum               minimus                最小值
| modulo                modulata               取模
| modulo_assign         modula                 取模赋值
| multiplied            multiplicata           已乘以
| multiply              multiplica             乘以
| named                 nominatus              命名分组
| negate                nega                   取负
| negated               negativa               已取负
| norm_layer            laminatio              层归一化
| norm_rms              rms_norm               rms_norm
| norm_rope             rope_norm              rope_norm
| normalize             normalizata            归一化
| power                 potentia               乘方
| put                   pone                   放入
| reduce                reducta                归约
| relu                  activatio_relu         ReLU
| remove_first          decapita               移除首项
| remove_last           detrahe                移除末项
| replace               muta                   替换
| reshape               forma                  重塑
| reverse               inverte                反转
| rope_half             rope_half              rope_half
| round                 rotunda                四舍五入
| set                   ponde                  设置
| shape                 magnitudines           形状
| shift                 disloco                平移
| shift_left            sinistra               左移
| shift_right           dextra                 右移
| shifted_left          sinistrata             已左移
| shifted_right         dextrata               已右移
| sign                  signum                 符号
| silu                  silu                   silu
| sin                   sinus                  正弦
| slice                 sectio                 切片
| softmax               activatio_softmax      Softmax
| softmax_causal        softmax_causal         Softmax_因果
| sort                  ordina                 排序
| sorted                ordinata               已排序
| split                 divide                 分割
| sqrt                  radix                  平方根
| start                 principium             起始
| starts_with           initium                开头是
| store                 store                  存储
| subtract              subtrahe               减去
| subtracted            subtracta              已减去
| sum                   summa                  求和
| swizzle               swizzle                swizzle
| take                  prima                  取前
| take_last             ultima                 取后
| tan                   tangens                正切
| text                  inventum               文本
| transpose             transpone              转置
| trim                  recide                 修剪空白
| truncate              trunca                 截断
| union                 unio                   并集
| union                 union                  并集
| uppercase             maiuscula              大写
| values                valores                值列表
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
