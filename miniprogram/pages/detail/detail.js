// detail.js
Page({
  data: {
    dishImage: "/pages/images/dish/dish1.jpg",
    selectedTab: 'recipe', // 初始选中的选项卡
    recipe: "乐山偷学技艺", // 菜谱内容
    ingredients: [ // 材料列表
      { name: "干辣椒", quantity: "50g" },
      { name: "花椒", quantity: "50g" },
      { name: "鸡腿", quantity: "3个" }
    ],
    method: "1. 买鸡 2. 炸鸡 3. 炒鸡", // 做法内容
    selectedTab: 'recipe', // 默认选中的tab，可以根据实际需求修改
  },
  
  selectTab(e) {
    const tab = e.currentTarget.dataset.tab;
    this.setData({
      selectedTab: tab,
    });
  },

  inputRecipe: function(event) {
    this.setData({ recipe: event.detail.value });
  },
  inputMethod: function(event) {
    this.setData({ method: event.detail.value });
  }
})
