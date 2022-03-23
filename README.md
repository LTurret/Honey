# Honey

Research of track honey source and species using a database.

# 之後再想要寫什麼 先放著

分類抓出tuple的最大、小值，在數據append的時候建立表格判斷tuple[0]出現的次數，再用次數去索取大小值  
table.count(tuple[0]) > 0 : 質量最大值  
table.count(tuple[0]) = 0 : 質量最小值

# 目標

- [x] 使用`Series`並建立索引表
- [ ] 使用`Series`整理並將相同`mass`的強度用`List`包起來
- [ ] 將所有`mass`的強度取出並設計**比對百分比**，製作有效比對模型
