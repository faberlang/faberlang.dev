+++
title = "Traditional Chinese reader locale"
section = "locales"
order = 17
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**繁體中文** — the `zh-Hant` reader pack. Script: Han (Traditional); direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `zh-Hant` |
| **Native name** | 繁體中文 |
| **Script** | Han (Traditional) |
| **Direction** | left-to-right |

A sibling pack, not a variant spelling: it carries different vocabulary (定值 against 常量) over the same semantics.

## English ↔ Traditional Chinese {#mapping}

Generated from the packs; read a row across to translate one term. The Latin column is the pack key, which keys the [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latin        繁體中文
| ---------------  -----------  --------------
| all              omnia        全部
| and              et           且
| annotation       annotatio    註解
| any              quilibet     任一
| argmax           argmaxima    最大值索引
| argmin           argminima    最小值索引
| args             argumenta    引數
| as               ut           作為
| asc              ascendens    升序
| assert           adfirma      斷言
| async            fiet         異步
| async_generator  fient        異流
| async_main       incipiet     非同步入口
| async_setup      praeparabit  準備非同步
| async_teardown   postparabit  後置準備非同步
| at               apud         在
| await            tacebit      等棄
| await_const      figendum     等定
| await_var        variandum    等變
| axis             axis         軸
| before           ante         之前
| bench            metior       測量
| between          inter        之間
| break            rumpe        中斷
| call             ad           端點
| case             casu         分支
| catch            cape         捕捉
| class            genus        類型
| cli              cli          命令行
| coalesce         vel          或取
| column           columna      欄位
| command          imperium     命令
| commands         imperia      命令集
| comptime         praefixum    前綴
| const            fixum        定值
| continue         perge        繼續
| conversion       conversio    轉換
| —                conversion   變換
| copy             exemplum     拷貝
| count            numeratio    計數
| cursor           cursor       迭代器
| debug            vide         檢視
| default          ceterum      預設
| desc             descendens   降序
| describe         probandum    測試規格
| description      descriptio   描述
| do               fac          執行
| elif             sin          否則若
| else             secus        否則
| embed            insere       嵌入
| empty            vacua        空集
| enum             ordo         列舉
| errors           errata       錯誤
| exit             exitus       出口
| expect_failure   erratur      預期失敗
| false            falsum       假
| flaky            fragilis     脆弱
| fn               functio      函式
| for              itera        遍歷
| format           scriptum     格式文字
| fragment         fragment     片段
| from             ex           取自
| future           futura       未來
| generator        fiunt        流
| global           ubique       全局
| guard            custodi      守衛
| if               si           若
| implements       implet       實作
| import           importa      匯入
| interface        implendum    待實作介面
| internal         interna      內部
| is               est          是
| kernel           nucleum      內核
| lambda           clausura     閉包
| lane             lane         車道
| let              sit          設為
| line             lineam       行
| long             longum       詳
| main             incipit      入口
| match            discerne     比對
| max              maxima       最大
| min              minima       最小
| module           regio        模組
| mut              varia        可變
| mut              varia        可變
| name             nomen        名稱
| nan              nonnumerus   nan
| not              non          非
| null             nulla        缺失
| only             solum        僅限
| only_in          solum_in     僅限於
| operand          operandus    操作數
| option           optio        選項
| optional         sponte       可選
| options          optiones     可選項
| or               aut          或
| own              penes        擁有
| panic            mori         崩潰
| pass             tacet        靜默
| per              pro          按
| primus_quem      primus_quem  primus_quem
| print            nota         註記
| private          privata      私有
| product          factum       求積
| protected        protecta     保護
| public           publica      公開
| radix            radix        radix
| range            ab           範圍
| read             lege         讀取
| readonly         immutata     不變
| reduce           reducta      歸約
| ref              de           從
| reject           reice        拒絕
| rename           verte        改名
| repeat           repete       重複
| require          requirit     需要
| rest             ceteri       其餘
| return           redde        傳回
| return_await     reddet       等返
| schema           schema       結構
| self             ego          自身
| setup            praepara     準備
| shared           commune      共享
| short            brevis       簡
| size             magnitudo    尺寸
| skip             omitte       略過
| sort             ordinata     排序
| spread           sparge       展開
| static           generis      靜態
| step             per          每
| sum              summa        求和
| switch           elige        選擇
| tag              tag          標籤
| teardown         postpara     後置準備
| test             proba        測試
| then             ergo         則
| thread           filum        執行緒
| throw            iace         拋出
| throws           iacit        可拋
| timeout          temporis     時限
| todo             futurum      預期
| trap             capta        陷阱
| true             verum        真
| tuple            iuncta       元組
| type             typus        型別
| ubi              ubi          ubi
| union            discretio    分支聯集
| unstable         nondum       不穩定
| until            usque        直到
| variant          finge        虛構
| version          versio       版本
| vertex           vertex       頂點
| via              via          經由
| warn             mone         警告
| while            dum          當
| within           intra        內含
| wrapping         modulus      模數
| write            scribe       寫出
| yield            cede         讓出
```

### Types {#types}

```text locale=la
| English      Latin        繁體中文
| -----------  -----------  ----------
| any          quidlibet    任意值
| ascii        ascii        ascii
| atomic       atomic       原子
| bool         bivalens     布林
| byte         octetus      單位元組
| bytes        octeti       位元組
| census       census       普查
| channel      sermo        通道
| char         littera      字元
| clamp        clampa       鉗制
| error        erratum      失誤
| filter       filtrum      篩選器
| float        fractus      小數
| frame        scrinium     幀
| instant      instans      執行個體
| int          numerus      整數
| iterator     cursor_t     游標
| json         json         JSON
| ledger       tabulae      帳本
| list         lista        列表
| map          tabula       表格
| matrix       matrix       矩陣
| never        numquam      永不
| none         nihil        無
| object       objectum     物件
| promise      promissum    承諾
| queue        queue        佇列
| range        intervallum  區間
| record       ratio        ratio
| recv         tuus         接收
| reflect      reflexa      反射
| regex        regex        正規表示式
| saturating   saturatus    飽和
| send         meus         發送
| series       series       序列
| set          copia        副本
| sparse       sparsa       稀疏
| stack        stack        堆疊
| string       textus       文字
| tensor       tensor       張量
| trapped      interceptum  受困
| trapping     exactus      精確
| unknown      ignotum      未知
| value        valor        值
| vector       vector       向量
| void         vacuum       空值
| wrap         involuta     環繞
| wrapping_ty  modulus_t    模數类型
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latin                  繁體中文
| --------------------  ---------------------  ------------
| abs                   absolutum              絕對值
| add                   adde                   新增
| added                 addita                 已新增
| added_bias            addita_bias            加偏置
| all                   omnia                  全部
| any                   quilibet               任一
| append                appende                附加
| apply                 applica                套用
| approx                approximata            近似
| argmax                argmaxima              最大值索引
| argmin                argminima              最小值索引
| at                    apud                   在
| at_least              maxime                 至少
| at_most               minime                 至多
| bit_and               coniuncta              位元與
| bit_and_assign        coniunge               位元與指派
| bit_or                disiuncta              位元或
| bit_or_assign         disiunge               位元或指派
| cbrt                  radix_cubica           立方根
| ceiling               tectum                 向上取整
| clamp                 coercere               限幅
| compare_exchange      compare_exchange       比較並交換
| complement            complementa            取補
| complemented          complementata          已取補
| contains              continet               包含
| cos                   cosinus                餘弦
| count_nonzero         nonnihil               非零個數
| create                crea                   建立
| cross                 transversum            叉積
| cross_entropy         crux_entropia          交叉熵
| cumulate              cumulata               累積
| cursor                cursor                 游標
| delete                dele                   刪除
| densify               densata                稠密化
| difference            differentia            差集
| difference_symmetric  symmetrica             對稱差集
| divide                divida                 除以
| divided               divisa                 已除以
| dot                   productum              點積
| drain                 exhauri                耗盡
| drop                  omissa                 捨棄
| end                   terminus               結束
| ends_with             finis                  結尾是
| escape                munita                 跳脫
| exchange              exchange               交換
| exp                   exponentia             指數
| expanded              expande                擴展
| fill                  reple                  填充
| filter                filtrata               過濾
| find                  inventa                尋找
| find_all              collecta               尋找全部
| finish                fini                   結束
| first                 primus                 第一個
| flatten               planata                展平
| flip                  alterna                翻轉
| flipped               alternata              已翻轉
| floor                 pavimentum             向下取整
| formata               formata                formata
| gather                gather                 收集
| gelu                  gelu                   gelu
| get                   accipe                 取得
| greater               maior                  大於
| group                 coetus                 分組
| has                   habet                  含有
| intersect             inter                  相交
| intersection          intersectio            交集
| invert                inversa                求逆
| is_empty              vacua                  為空
| is_subset             subcopia               是子集
| is_superset           supercopia             是超集
| keys                  claves                 鍵列表
| last                  ultimus                最後一個
| length                longitudo              長度
| less                  minor                  小於
| limes                 limes                  邊界
| ln                    logarithmus            自然對數
| load                  load                   載入
| log10                 logarithmus_decimalis  常用對數
| lowercase             minuscula              小寫
| map                   mappata                變換
| matches               consentit              比對
| materialize           materialize            物化
| matmul                matmul                 矩陣乘法
| maximum               maximus                最大值
| mean                  media                  平均值
| minimum               minimus                最小值
| modulo                modulata               取餘
| modulo_assign         modula                 取餘指派
| multiplied            multiplicata           已乘以
| multiply              multiplica             乘以
| named                 nominatus              命名分組
| negate                nega                   取負
| negated               negativa               已取負
| norm_layer            laminatio              層正規化
| norm_rms              rms_norm               rms_norm
| norm_rope             rope_norm              rope_norm
| normalize             normalizata            正規化
| power                 potentia               乘冪
| put                   pone                   放入
| reduce                reducta                歸約
| relu                  activatio_relu         ReLU
| remove_first          decapita               移除首項
| remove_last           detrahe                移除末項
| replace               muta                   替換
| reshape               forma                  重塑
| reverse               inverte                反轉
| rope_half             rope_half              rope_half
| round                 rotunda                四捨五入
| set                   ponde                  設定
| shape                 magnitudines           形狀
| shift                 disloco                平移
| shift_left            sinistra               左移
| shift_right           dextra                 右移
| shifted_left          sinistrata             已左移
| shifted_right         dextrata               已右移
| sign                  signum                 符號
| silu                  silu                   silu
| sin                   sinus                  正弦
| sink                  immerge                浸入
| slice                 sectio                 切片
| softmax               activatio_softmax      Softmax
| softmax_causal        softmax_causal         Softmax_因果
| sort                  ordina                 排序
| sorted                ordinata               已排序
| split                 divide                 分割
| sqrt                  radix                  平方根
| start                 principium             起始
| starts_with           initium                開頭是
| store                 store                  儲存
| subtract              subtrahe               減去
| subtracted            subtracta              已減去
| sum                   summa                  求和
| swizzle               swizzle                swizzle
| take                  prima                  取前
| take_last             ultima                 取後
| tan                   tangens                正切
| text                  inventum               文字
| transpose             transpone              轉置
| trim                  recide                 修剪空白
| truncate              trunca                 截斷
| union                 unio                   聯集
| union                 union                  聯集
| uppercase             maiuscula              大寫
| values                valores                值列表
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
