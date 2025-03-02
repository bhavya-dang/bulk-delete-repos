while read -r r; do
    curl -X DELETE -H "Authorization: token <token>" "https://api.github.com/repos/$r"
done < repos

echo "All repositories have been successfully deleted!"
