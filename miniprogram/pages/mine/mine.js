// pages/mine/mine.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userName: "Owen.T",
    userAvatar: "/pages/images/avatar.jpg", // 用户头像地址
    backgroundImage: '/pages/images/background.jpg', // 背景图片地址
    dishCount: 0,
    fansCount: 0,
    personalDescription: "个人描述XXXXXXXX",
    category: "菜品分类",
    dishes: [
      { name: "川菜", image: "/pages/images/dish1.jpg" },
      { name: "粤菜", image: "/pages/images/dish2.jpg" },
      { name: "湘菜", image: "/pages/images/dish3.jpg" }
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})