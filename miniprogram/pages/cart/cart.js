// pages/cart/cart.js

Page({
  data: {
    materials: [
      { name: "苹果", category: "水果", quantity: 5, currency: "￥", price: 2.5 },
      { name: "牛奶", category: "饮品", quantity: 2, currency: "￥", price: 5 },
      { name: "鸡蛋", category: "肉蛋", quantity: 12, currency: "￥", price: 3 }
    ]
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
  },

  // 删除按钮点击事件，删除材料
  deleteMaterial: function (event) {
    const index = event.currentTarget.dataset.index;
    const materials = this.data.materials;
    materials.splice(index, 1);
    this.setData({
      materials: materials
    });
  }
});
