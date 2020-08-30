package com.qw.springCloudClientTest.modules.test.dao;

import com.qw.springCloudClientTest.modules.test.pojo.City;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * ClassName: CityDao <br/>
 * Description: <br/>
 * date: 2020/8/11 22:02<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@Repository
@Mapper
public interface CityDao {
    //通过id查询
    @Select("select * from m_city where country_id = #{countryId}")
    List<City> getCitiesByCountryId(int countryId);

}
