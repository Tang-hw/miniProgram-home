// detail.js
Page({
  data: {
    dishImage: "/pages/images/dish/dish1.jpg",
    selectedTab: 'recipe', // 初始选中的选项卡
    recipe: "乐山偷学技艺", // 菜谱内容
    ingredients: [ // 材料列表
      { name: "干辣椒", quantity: "50" ,unit:"g" },
      { name: "花椒", quantity: "50" ,unit:"g" },
      { name: "鸡腿", quantity: "3" ,unit:"个" }
    ],
    method: "第一步：买鸡 第二步：炸鸡 第三步：炒鸡", // 做法内容
  },
  

  inputRecipe: function(event) {
    this.setData({ recipe: event.detail.value });
  },

  inputMethod: function(event) {
    this.setData({ method: event.detail.value });
  }
})
