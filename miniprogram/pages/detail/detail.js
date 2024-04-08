// detail.js
Page({
  data: {
    dishImage: "/path/to/dish.jpg",
    selectedTab: 'recipe', // 初始选中的选项卡
    recipe: "", // 菜谱内容
    ingredients: [ // 材料列表
      { name: "材料1", quantity: "100g" },
      { name: "材料2", quantity: "200g" },
      { name: "材料3", quantity: "1个" }
    ],
    method: "" // 做法内容
  },
  switchTab: function(event) {
    const tab = event.currentTarget.dataset.tab;
    this.setData({ selectedTab: tab });
  },
  inputRecipe: function(event) {
    this.setData({ recipe: event.detail.value });
  },
  inputMethod: function(event) {
    this.setData({ method: event.detail.value });
  }
})
