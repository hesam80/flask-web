import {useState, useEffect} from 'react'

const useDarkMode = ()=> {
	const [theme,setTheme]=useState('light')

	const toggleTheme= ()=>{
		if (theme==='light') {
			window.localStorage.setItem('theme','dark')
			setTheme('dark')
		}
		else{
			window.localStorage.setItem('theme', 'light')
			setTheme('light')
		}
	}

	useEffect(()=> {
        // eslint-disable-next-line
		const localTheme = window.localStorage.getItem('theme')
	}, [])
	return [theme, toggleTheme]
}
export default useDarkMode