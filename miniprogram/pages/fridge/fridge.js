// pages/fridge/fridge.js

Page({
  data: {
    materials: [
      { id:1, name: "苹果", category: "水果", quantity: 5, currency: "￥", price: 2.5, expiry: 3, purchaseDate:"2024-04-1", expiryDate: "2024-04-10", image: "/pages/images/fridge/apple.jpg" },
      {  id:2, name: "牛奶", category: "饮品", quantity: 2, currency: "￥", price: 5, expiry: 2, purchaseDate:"2024-04-1", expiryDate: "2024-04-09", image: "/pages/images/fridge/milk.jpg" },
      {  id:3, name: "鸡蛋", category: "肉蛋", quantity: 12, currency: "￥", price: 3, expiry: 5, purchaseDate:"2024-04-1", expiryDate: "2024-04-12", image: "/pages/images/fridge/egg.jpg" }
    ],
    showPopup: false, // 控制弹窗显示与隐藏
    selectedMaterial: null // 选中的材料
  },

   // 点击材料图片，显示弹窗
   showClass: function (event) {
    const index = event.currentTarget.dataset.index;
    const material = this.data.materials[index];
    this.setData({
      showPopup: true,
      selectedMaterial: material
    });
    console.log(1);
  },

  // 点击弹窗外部或退出按钮，隐藏弹窗
  hideClass: function () {
    this.setData({
      showPopup: false
    });
    console.log(2);
  },

  // 点击保存按钮，保存材料信息（示例）
  saveMaterial: function () {
    console.log("保存材料信息");
  },

  // 加号按钮点击事件，新增材料
  addMaterial: function () {
    // 这里可以实现新增材料的逻辑，例如弹出新增材料的对话框
    console.log("新增材料");
  },

  // 减号按钮点击事件，减少材料数量
  minusQuantity: function (event) {
    const index = event.currentTarget.dataset.index;
    const materials = this.data.materials;
    if (materials[index].quantity > 0) {
      materials[index].quantity--;
      this.setData({
        materials: materials
      });
    }
  },

  // 加号按钮点击事件，增加材料数量
  plusQuantity: function (event) {
    const index = event.currentTarget.dataset.index;
    const materials = this.data.materials;
    materials[index].quantity++;
    this.setData({
      materials: materials
    });
  }
});
