package com.qw.springCloudZuul.filter;

import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;
import com.netflix.zuul.exception.ZuulException;
import org.apache.commons.lang.StringUtils;
import org.apache.http.HttpStatus;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServletRequest;

/**
 * ClassName: UserLoginZuulFilter <br/>
 * Description: <br/>
 * date: 2020/8/31 14:38<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@Component
public class UserLoginZuulFilter extends ZuulFilter {

    /**
     * 过滤器类型
     */
    @Override
    public String filterType() {
        return "pre";
    }

    /**
     * 过滤器优先级
     */
    @Override
    public int filterOrder() {
        return 0;
    }

    /**
     * 是否执行该过滤器
     */
    @Override
    public boolean shouldFilter() {
        return true;
    }

    /**
     * 过滤器业务逻辑
     */
    @Override
    public Object run() throws ZuulException {
        RequestContext requestContext = RequestContext.getCurrentContext();
        HttpServletRequest request = requestContext.getRequest();
        String token  = request.getParameter("token");
        //token 为空或者是不等于 hyman 的情况下，设置响应
        if (StringUtils.isBlank(token) || !"hyman".equalsIgnoreCase(token)){
            // 过滤该请求，不对其进行路由
            requestContext.setSendZuulResponse(false);
            // 设置响应状态码
            requestContext.setResponseStatusCode(HttpStatus.SC_UNAUTHORIZED);
            // 设置响应内容
            requestContext.setResponseBody("Token is null or error.");
        }

        return null;
    }
}
