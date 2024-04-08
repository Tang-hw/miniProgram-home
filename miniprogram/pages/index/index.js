// index.js
Page({
  data: {
    dishes: [
      { name: "歌山辣子鸡", category: "川菜", image: "/pages/images/dish1.jpg" , userName: "Owen.T", userAvatar: "/pages/images/avatar.jpg", like:"7"},
      { name: "腊肠煲仔饭", category: "粤菜", image: "/pages/images/dish2.jpg",  userName: "Owen.T", userAvatar: "/pages/images/avatar.jpg", like:"8"},
      { name: "小炒黄牛肉", category: "湘菜", image: "/pages/images/dish3.jpg" , userName: "Owen.T", userAvatar: "/pages/images/avatar.jpg", like:"9"}
    ]
  },
  gotoEditUserInfo: function(event) {
    wx.navigateTo({
      url: '/pages/editUserInfo/editUserInfo'
    })
  },
  gotoDetail: function(event) {
    // 跳转至菜品详情页
  }
})
