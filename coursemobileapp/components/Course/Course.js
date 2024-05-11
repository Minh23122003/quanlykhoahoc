import MyStyles from "../../styles/MyStyles"
import {View, Text, ActivityIndicator, Image, left} from "react-native"
import React from "react"
import APIs, { endpoints } from "../../configs/APIs";
import { Chip, List } from "react-native-paper";


const Course = () => {
    const [categories, setCategories] = React.useState(null);
    const [courses, setCourses] = React.useState([]);
    const [loading, setLoading] = React.useState(false);

    const loadCates = async () => {
        try {
            let res = await APIs.get(endpoints['categories']);
            setCategories(res.data);
        } catch(ex){
            console.error(ex)
        }
    }

    const loadCourses = async () => {
        try {
            setLoading(true);
            let res = await APIs.get(endpoints['courses']);
            setCourses(res.data.results);
        } catch(ex){
            console.error(ex)
        } finally {
            setLoading(false);
        }
    }

    React.useEffect(() => {
        loadCates();
    }, []);

    React.useEffect(() => {
        loadCourses();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>Danh muc khoa hoc</Text>
            <View style={MyStyles.row}>
                {categories===null?<ActivityIndicator/>:<>
                    {categories.map(c => <Chip style={MyStyles.margin} key={c.id} icon="shape">{c.name}</Chip>)}
                </>}
            </View>

            <View>
                {courses.map(c => <List.Item style={MyStyles.margin} key={c.id} title={c.subject} description={moment(c.created_date).fromNow()} left={() => <Image style={MyStyles.avatar} source={{uri: c.image}} />} />)}
                {loading && <ActivityIndicator/>}
            </View>
        </View>
    )
}

export default Course;
