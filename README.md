# Api Testing
  API is the brain of our connected world. It is the set of tools, protocols, standards and code that glues our digital world together. APIs allow for companies to become more agile, for things to go mobile, and everything to work together in a streamlined, integrated way.The API Testing is performed for the system, which has a collection of API that ought to be tested.
  
  ## What to be tested
   * Status code of api's (200,400,500,502 etc)
   * Response time of an api
   * Exploring boundary conditions and ensuring that the test harness varies parameters of the API calls in ways that verify functionality and expose failures.
   * Return Value based on input condition - The return value from the API's are checked based on the input condition.
   * Verify if the API is updating any data structure.
   * Verifying the Sequence of API calls and check if the API's produce useful results from successive calls.
   * Authrization and authenticaton 
   
  ## Set Environment 
   The first part of API testing involves setting up a testing environment, with the required set of parameters around the API.Once you’ve set up your API testing environment, make an API call right away to make sure nothing is broken before you go forward to start your more thorough testing.I have used [postman](https://www.getpostman.com/apps) for api testing, [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-use-postman-to-call-api.html) is the link for step by step instruction for an api call using postman.
   
  ## Automation testing of Rest api 
   One of Postman's most powerful features is its ability to run automated tests on your requests. To get started quickly here is the postman's [tutorial](http://blog.getpostman.com/2017/07/28/api-testing-tips-from-a-postman-professional/).Using this tutorial user will able to write automated test scrpit for api.
   
   ### Example
   Below is the sample of my basic automation test scripts for an api to check response time, status code, header and body, for advance assertion please check the [collection file](https://github.com/Akanksha461/API-Testing-Framework/blob/master/Totojitu-New1.postman_collection) and [environment file](https://github.com/Akanksha461/API-Testing-Framework/blob/master/Totojitu.postman_environment) of my project.You can add many more assertion,I have used chai assertion along with javascript.
   
   ```
 eval(globals.postmanBDD);

//response assertion
describe('assertion for response',()=>{
    it('checks response code',()=>{
      response.should.have.status(400); 
    });
    it('checks response time',()=>{
        response.time.should.be.below(1000);
    });
    
    it('response should be in Html format',()=>{
      response.should.be.html;
    });
    it('should be an error response', () => {      
        response.error.should.be.true; 
    });  
    it("doesn't return a HTTP 200 code",()=>{   
        response.should.not.have.status(200); 
    });
    it("doesn't send a OK response",()=>{      
         response.ok.should.be.false;    
         
    });
    it("should return a client error",()=>{  
         response.clientError.should.be.true;
    });
    it("should not return a server error",()=>{ 
        response.serverError.should.be.false; 
    });
    it("should return a 4xx status code",()=>{  
        response.statusType.should.equal(4);
    });
    
});
//header asserstion
describe('check for header block',()=>{
    
    it('access control allow origin should be "*',()=>{
        response.should.have.header('access-control-allow-origin',"*");
    });
    
    it('CF-RAY should not be empty',()=>{
        response.should.have.header('CF-RAY').should.not.be.empty;
    });
    
    it('web server should support keep-alive connections',()=>{
        response.should.have.header('Connection','keep-alive');
    });
    
    it('content type shpuld be apllication/json',()=>{
        response.should.have.header('Content-Type', 'text/html; charset=utf-8');
    });
    
    it('Date should not be empty',()=>{
        response.should.have.header('Date').and.not.empty; 
    });
    
    it('server should be cloudflare-nginx',()=>{
        response.should.have.header('Server','cloudflare-nginx');
    });
    
    it('server should be Transfer-Encoding',()=>{
        response.should.have.header('Transfer-Encoding','chunked');
    });
    
    it('vary should be Accept-Encoding',()=>{
        response.should.have.header('Vary','Accept-Encoding');
    });
    it('X-Powered-By should be an Express',()=>{
        response.should.have.header('X-Powered-By' ,'Express');
    });
   
});

//body asserstion
describe('checks for body',()=>{
    it('response body should not be empty',()=>{
      response.body.should.and.not.empty; 
    });
    it('response body should be in html format',()=>{
      response.should.be.html;
    });
    it('response body should be user does not exist',()=>{
      response.body.should.equal('user does not exist');
    });
});
 ```
 # Jenkins
   Jenkins is a software that allows continuous integration we use Jenkins to automate your development workflow so you can focus on work that matters most. [Here](https://www.youtube.com/watch?v=g_4SX7oeyJc) is jenkins link for step by step istallation process. I have integrated my code with jenkins and set the time to make build on daily basis using cron.
   






