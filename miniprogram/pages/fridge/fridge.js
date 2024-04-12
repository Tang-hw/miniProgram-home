// pages/fridge/fridge.js

Page({
  data: {
    categorys:[
      { id:1, 
        name:"水果",
        materials: [
        { id:1, name: "苹果", category: "水果", quantity: 5, currency: "￥", price: 2.5, expiry: 3, purchaseDate:"2024-04-1", expiryDate: "2024-04-10", image: "/pages/images/fridge/apple.jpg" },
        {  id:2, name: "葡萄", category: "水果", quantity: 2, currency: "￥", price: 32, expiry: 2, purchaseDate:"2024-04-1", expiryDate: "2024-04-09", image: "/pages/images/fridge/grape.jpg" }],
      },

      { id:2, 
        name:"饮品",
        materials: [
          { id:1, name: "可乐", category: "饮品", quantity: 5, currency: "￥", price: 3, expiry: 3, purchaseDate:"2024-04-1", expiryDate: "2024-04-10", image: "/pages/images/fridge/coke.jpg" },
          {  id:2, name: "牛奶", category: "饮品", quantity: 2, currency: "￥", price: 5, expiry: 2, purchaseDate:"2024-04-1", expiryDate: "2024-04-09", image: "/pages/images/fridge/milk.jpg" }],
      },

      { id:3, 
        name:"肉蛋",
        materials: [
          { id:1, name: "牛肉", category: "肉蛋", quantity: 5, currency: "￥", price: 98, expiry: 3, purchaseDate:"2024-04-1", expiryDate: "2024-04-10", image: "/pages/images/fridge/beef.jpg" },
          {  id:2, name: "鸡蛋", category: "肉蛋", quantity: 12, currency: "￥", price: 15, expiry: 5, purchaseDate:"2024-04-1", expiryDate: "2024-04-12", image: "/pages/images/fridge/egg.jpg"}],
      }
    ],

  },


  
});
