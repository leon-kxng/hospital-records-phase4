const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/hospitals', // or any other API endpoint
    createProxyMiddleware({
      target: 'https://hospital-records.replit.app',
      changeOrigin: true,
    })
  );
};
